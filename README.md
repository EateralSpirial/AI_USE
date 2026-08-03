# AI_USE

AI_USE is the canonical public repository for synchronizing a user's global agent context across devices. The initial implementation targets Codex.

## Repository contract

| Repository object | Local Codex destination | Purpose |
| --- | --- | --- |
| `AGENTS.md` | `$CODEX_HOME/AGENTS.md` or `~/.codex/AGENTS.md` | Global instructions shared across projects |
| `skills/*` | `$CODEX_HOME/skills/*` | Reusable global workflows |
| `experiences/*` | Repository only | Sanitized, durable, cross-project operating experience |

The `main` branch is the canonical distribution source.

## Included skills

### `update-global-agent-context`

Installs, updates, repairs, or verifies the current device's Codex global context from this repository. It validates the source, preserves unmanaged local skills, creates backups, and reports the installed commit.

### `publish-global-agent-experience`

Converts execution experience into a reusable global entry and submits it to this repository. It may run only after the user explicitly authorizes publication. Its default publication path is a branch and pull request; direct writes to `main` require explicit instruction.

## Initial installation

Clone the repository and run the bundled synchronizer:

```bash
git clone https://github.com/EateralSpirial/AI_USE.git
cd AI_USE
python skills/update-global-agent-context/scripts/sync.py --source .
```

On Windows, `py` can replace `python`.

## Later updates

A local agent can invoke `update-global-agent-context`, or the installed script can fetch `main` directly:

```bash
python ~/.codex/skills/update-global-agent-context/scripts/sync.py --remote
```

Set `CODEX_HOME` when Codex uses a non-default global directory.

## Publication policy

Global experience is opt-in. Routine sessions, project-local implementation details, credentials, private paths, personal data, and proprietary material stay outside this repository. Every published entry must state its trigger conditions, reusable procedure, verification method, and limits.
