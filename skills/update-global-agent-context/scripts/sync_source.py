"""Acquire and validate the AI_USE source repository."""

import argparse
import subprocess
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

REMOTE_URL = "https://github.com/EateralSpirial/AI_USE.git"
REMOTE_NAME = "EateralSpirial/AI_USE"
DEFAULT_REF = "main"
REQUIRED_SKILLS = {
    "update-global-agent-context",
    "publish-global-agent-experience",
}


class SyncError(RuntimeError):
    """Raised when source validation or installation cannot complete safely."""


@contextmanager
def acquire_source(args: argparse.Namespace) -> Iterator[Path]:
    if args.source is not None:
        source = args.source.expanduser().resolve()
        if not source.is_dir():
            raise SyncError(f"Source directory does not exist: {source}")
        yield source
        return

    try:
        with tempfile.TemporaryDirectory(prefix="ai-use-source-") as temp_dir:
            checkout = Path(temp_dir) / "AI_USE"
            command = [
                "git",
                "clone",
                "--depth",
                "1",
                "--branch",
                args.ref,
                REMOTE_URL,
                str(checkout),
            ]
            subprocess.run(command, check=True, capture_output=True, text=True)
            yield checkout
    except FileNotFoundError as exc:
        raise SyncError("git is required for remote synchronization") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or str(exc)).strip()
        raise SyncError(f"Unable to clone {REMOTE_URL}: {detail}") from exc


def read_frontmatter(skill_file: Path) -> dict[str, str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise SyncError(f"Missing YAML frontmatter: {skill_file}")

    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"\'')
    else:
        raise SyncError(f"Unterminated YAML frontmatter: {skill_file}")
    return metadata


def validate_source(source: Path) -> list[Path]:
    agents_file = source / "AGENTS.md"
    if not agents_file.is_file() or not agents_file.read_text(encoding="utf-8").strip():
        raise SyncError(f"Missing or empty AGENTS.md in {source}")

    skills_root = source / "skills"
    if not skills_root.is_dir():
        raise SyncError(f"Missing skills directory in {source}")

    skill_dirs: list[Path] = []
    for child in sorted(skills_root.iterdir(), key=lambda path: path.name):
        if not child.is_dir():
            continue
        skill_file = child / "SKILL.md"
        if not skill_file.is_file():
            continue
        metadata = read_frontmatter(skill_file)
        if metadata.get("name") != child.name:
            raise SyncError(
                f"Skill name mismatch for {skill_file}: "
                f"expected {child.name!r}, found {metadata.get('name')!r}"
            )
        if not metadata.get("description"):
            raise SyncError(f"Skill description is missing: {skill_file}")
        skill_dirs.append(child)

    found = {path.name for path in skill_dirs}
    missing = sorted(REQUIRED_SKILLS - found)
    if missing:
        raise SyncError(f"Required managed skills are missing: {', '.join(missing)}")
    return skill_dirs


def git_commit(source: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(source), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    value = result.stdout.strip()
    return value or None
