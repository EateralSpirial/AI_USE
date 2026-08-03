"""Plan and apply AI_USE-managed Codex global context changes."""

import json
import shutil
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

from sync_fs import content_digest, copy_path, load_json, remove_path, replace_from_stage
from sync_source import REMOTE_NAME, git_commit, validate_source


def install(source: Path, codex_home: Path, ref: str, dry_run: bool) -> dict[str, object]:
    skill_dirs = validate_source(source)
    source_commit = git_commit(source)

    assets: list[tuple[str, Path, Path]] = [
        ("AGENTS.md", source / "AGENTS.md", codex_home / "AGENTS.md")
    ]
    for skill_dir in skill_dirs:
        relative = f"skills/{skill_dir.name}"
        assets.append((relative, skill_dir, codex_home / relative))

    changed_assets = [
        relative
        for relative, source_path, target_path in assets
        if content_digest(source_path) != content_digest(target_path)
    ]
    unchanged_assets = [relative for relative, _, _ in assets if relative not in changed_assets]

    desired_identity: dict[str, object] = {
        "schema_version": 1,
        "repository": REMOTE_NAME,
        "ref": ref,
        "source_commit": source_commit,
        "managed_skills": [path.name for path in skill_dirs],
    }
    state_path = codex_home / ".ai-use-state.json"
    current_state = load_json(state_path)
    current_identity = None
    if current_state is not None:
        current_identity = {key: current_state.get(key) for key in desired_identity}
    state_changed = current_identity != desired_identity

    changed = list(changed_assets)
    if state_changed:
        changed.append(".ai-use-state.json")

    result: dict[str, object] = {
        "repository": REMOTE_NAME,
        "ref": ref,
        "source_commit": source_commit,
        "codex_home": str(codex_home),
        "managed_skills": desired_identity["managed_skills"],
        "changed": changed,
        "unchanged": unchanged_assets,
        "dry_run": dry_run,
        "backup": None,
    }
    if dry_run or not changed:
        return result

    codex_home.parent.mkdir(parents=True, exist_ok=True)
    codex_home.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_id = f"{timestamp}-{uuid.uuid4().hex[:8]}"
    backup_root = codex_home / "backups" / "ai-use" / backup_id
    stage_root = Path(
        tempfile.mkdtemp(prefix=".ai-use-stage-", dir=str(codex_home.parent))
    )

    targets: list[tuple[str, Path, Path]] = []
    existed: dict[str, bool] = {}
    try:
        for relative, source_path, target_path in assets:
            if relative not in changed_assets:
                continue
            staged_path = stage_root / relative
            copy_path(source_path, staged_path)
            targets.append((relative, staged_path, target_path))

        if state_changed:
            state = dict(desired_identity)
            state["installed_at"] = datetime.now(timezone.utc).isoformat()
            staged_state = stage_root / ".ai-use-state.json"
            staged_state.write_text(
                json.dumps(state, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            targets.append((".ai-use-state.json", staged_state, state_path))

        for relative, _, target_path in targets:
            existed[relative] = target_path.exists() or target_path.is_symlink()
            if existed[relative]:
                copy_path(target_path, backup_root / relative)

        applied: list[tuple[str, Path]] = []
        try:
            for relative, staged_path, target_path in targets:
                applied.append((relative, target_path))
                replace_from_stage(staged_path, target_path)
        except Exception:
            for relative, target_path in reversed(applied):
                if target_path.exists() or target_path.is_symlink():
                    remove_path(target_path)
                backup_path = backup_root / relative
                if existed.get(relative) and backup_path.exists():
                    copy_path(backup_path, target_path)
            raise

        result["backup"] = str(backup_root) if backup_root.exists() else None
        return result
    finally:
        shutil.rmtree(stage_root, ignore_errors=True)
