# AI_USE

AI_USE is a user-level agent context kernel. It supplies compact, portable context material and the skills that let a user's local agents keep their global working context current and selectively learn from experience.

## System Model

The repository and the local environment have distinct ownership:

- **AI_USE** carries portable principles, example global instructions, reusable skills, and broadly useful cross-project experience.
- **The user's local agent context** carries the personalized working state: user-specific preferences, local environment knowledge, and accepted experience accumulated during use.
- **Each project** carries its own architecture, contracts, workflows, and project-specific lessons.

This separation keeps the public source reusable while allowing each local context system to evolve around its user.

## Canonical Objects

| Object | Role |
| --- | --- |
| [`PRINCIPLES.md`](PRINCIPLES.md) | Canonical principles governing user-level context design and evolution |
| [`AGENTS.md`](AGENTS.md) | Demonstrative global instructions and a compact route into context evolution |
| [`sync-user-agent-context`](skills/sync-user-agent-context/SKILL.md) | Reconcile AI_USE material into the current user's local global agent context |
| [`evolve-user-agent-context`](skills/evolve-user-agent-context/SKILL.md) | Evaluate execution experience and evolve the user's local context |

The repository stays compact. New files and skills appear when a durable meaning requires a distinct owner.

## Operating Loop

1. Install the two skills into the user's global agent skill library.
2. Use `sync-user-agent-context` to onboard or refresh a device from AI_USE.
3. Let agents work normally with project-local context and direct evidence.
4. Invoke `evolve-user-agent-context` after a strong experience trigger.
5. Integrate accepted lessons into the narrowest canonical local owner.
6. When a lesson is broadly reusable across users and projects, ask the user whether to contribute it back to AI_USE.

## Installation

Install each skill with Codex's skill installer:

```text
$skill-installer install https://github.com/EateralSpirial/AI_USE/tree/main/skills/sync-user-agent-context
$skill-installer install https://github.com/EateralSpirial/AI_USE/tree/main/skills/evolve-user-agent-context
```

Then invoke:

```text
Use $sync-user-agent-context to initialize or refresh my global agent context from AI_USE.
```

## Conceptual Lineage

AI_USE adapts the onboarding-first context principles developed in [`agent-context-kernel`](https://github.com/EateralSpirial/agent-context-kernel) to the user level. Its selective experience loop develops the earlier self-evolution direction explored in [`central-skill-seed`](https://github.com/EateralSpirial/central-skill-seed).
