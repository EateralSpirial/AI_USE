#!/usr/bin/env python3
"""Synchronize AI_USE-managed Codex global context onto the current device."""

import argparse
import json
import os
import sys
from pathlib import Path

from sync_install import install
from sync_source import DEFAULT_REF, SyncError, acquire_source


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install AI_USE-managed AGENTS.md and skills into CODEX_HOME."
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument(
        "--source",
        type=Path,
        help="Existing AI_USE repository checkout to install from.",
    )
    source.add_argument(
        "--remote",
        action="store_true",
        help="Clone the configured GitHub repository into a temporary directory.",
    )
    parser.add_argument(
        "--ref",
        default=DEFAULT_REF,
        help=f"Remote branch or tag to clone (default: {DEFAULT_REF}).",
    )
    parser.add_argument(
        "--codex-home",
        type=Path,
        help="Destination Codex home. Defaults to CODEX_HOME or ~/.codex.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and report changes without modifying the destination.",
    )
    return parser.parse_args()


def resolve_codex_home(value: Path | None) -> Path:
    if value is not None:
        return value.expanduser().resolve()
    configured = os.environ.get("CODEX_HOME")
    if configured:
        return Path(configured).expanduser().resolve()
    return (Path.home() / ".codex").resolve()


def main() -> int:
    args = parse_args()
    codex_home = resolve_codex_home(args.codex_home)
    try:
        with acquire_source(args) as source:
            result = install(source, codex_home, args.ref, args.dry_run)
    except (SyncError, OSError, ValueError) as exc:
        print(f"AI_USE sync failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
