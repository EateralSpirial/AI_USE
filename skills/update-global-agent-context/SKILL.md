---
name: update-global-agent-context
description: Install, update, repair, or verify the current device's Codex global AGENTS.md and AI_USE-managed skills from the public EateralSpirial/AI_USE repository. Use when the user asks to pull, download, refresh, synchronize, bootstrap, repair, or inspect the global Codex context on a device.
---

# Update Global Agent Context

## Purpose

Treat `EateralSpirial/AI_USE` branch `main` as the canonical source for the user's global Codex context and apply its managed objects to the current device.

## Managed objects

- Repository `AGENTS.md` -> `${CODEX_HOME:-~/.codex}/AGENTS.md`
- Every repository directory matching `skills/*/SKILL.md` -> `${CODEX_HOME:-~/.codex}/skills/<skill-name>/`
- Synchronizer state -> `${CODEX_HOME:-~/.codex}/.ai-use-state.json`

Preserve every local skill whose name is absent from the repository.

## Workflow

1. Resolve `CODEX_HOME`. Use the environment variable when set; otherwise use `~/.codex`.
2. Select the source:
   - From an existing AI_USE checkout, run `scripts/sync.py --source <repository-root>`.
   - Otherwise run `scripts/sync.py --remote` to clone `main` into a temporary directory.
3. Use `--dry-run` first when the user asks only to inspect or verify synchronization.
4. Read the script's JSON result. Confirm the source commit, destination, changed objects, and backup location.
5. After a real update, verify that the destination `AGENTS.md` exists and each reported skill contains a valid `SKILL.md`.
6. Tell the user to start a new Codex session when immediate instruction or skill rediscovery matters.

## Safety and consistency rules

- Validate the complete source before changing the destination.
- Back up every managed destination that will be replaced.
- Replace remote-managed objects as canonical units; retain the backup instead of silently merging local edits.
- Leave unmanaged local skills untouched.
- Leave the destination unchanged when validation fails.
- Use only the configured AI_USE repository as the remote source.
- This skill performs download and local installation only. It never uploads local experience or repository changes.

## Commands

From this skill directory:

```bash
python scripts/sync.py --remote
python scripts/sync.py --remote --dry-run
python scripts/sync.py --source /path/to/AI_USE
```

Use `--codex-home <path>` only when the destination differs from `CODEX_HOME` and `~/.codex`.
