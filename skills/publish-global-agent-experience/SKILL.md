---
name: publish-global-agent-experience
description: Summarize durable cross-project agent-operating experience and submit it to EateralSpirial/AI_USE only when the user explicitly asks to upload, publish, contribute, or commit that experience. Do not use for routine session summaries, project-local lessons, or implicit suggestions.
---

# Publish Global Agent Experience

## Authorization gate

Run this workflow only when the user explicitly authorizes publication in the current task. A useful lesson, a completed task, or a standing preference to improve agents does not by itself authorize an upload.

When authorization is absent, keep the experience local and perform no repository write.

## Acceptance criteria

Publish an experience only when it is:

- applicable across multiple repositories, devices, or agent sessions;
- durable enough to remain useful beyond the current task;
- expressible as concrete trigger conditions, a procedure, and verification;
- sanitized for a public repository;
- meaningfully distinct from existing entries.

Exclude project-specific architecture, one-off debugging details, credentials, tokens, private repository content, personal data, proprietary material, machine-specific secrets, and copied third-party text.

## Target format

Create `experiences/YYYY-MM-DD-<short-kebab-case-slug>.md` with this structure:

```markdown
---
title: <concise title>
date: YYYY-MM-DD
status: proposed
scope: global
applies_to:
  - <agent or workflow class>
---

# <Title>

## Observation

<Sanitized evidence from the execution process.>

## Generalized principle

<The durable rule or model.>

## Trigger conditions

<When an agent should apply it.>

## Procedure

<Concrete ordered workflow.>

## Verification

<How to determine that the procedure worked.>

## Limits

<Contexts where the experience is uncertain, inapplicable, or requires escalation.>

## Provenance

- Publication explicitly authorized by the user in the originating task.
- Content generalized and sanitized by an agent before submission.
```

Update the index table in `experiences/README.md` in the same change.

## Workflow

1. Confirm that the current task contains explicit publication authorization.
2. Inspect the relevant execution record and extract only global, reusable lessons.
3. Search `experiences/` for overlapping principles. Extend an existing entry when that produces a single canonical statement; otherwise create a new entry.
4. Remove secrets, private identifiers, exact local paths, private repository names, user data, and unnecessary implementation detail.
5. Draft the experience using the target format. Separate observed evidence from the generalized conclusion.
6. Verify every command, path, or behavioral claim that can be checked locally.
7. Update `experiences/README.md`.
8. Run repository validation available in the checkout, then inspect the final diff.
9. Commit with `docs(experience): add <slug>` or `docs(experience): refine <slug>`.
10. Unless the user explicitly requests a direct update to `main`, push a branch named `experience/YYYY-MM-DD-<slug>` and open a pull request.
11. Report the commit or pull-request URL and summarize the sanitized content that was published.

## Publication boundaries

- User authorization controls whether publication occurs.
- A public repository requires aggressive sanitization.
- Prefer one canonical entry per principle.
- Preserve uncertainty and scope limits.
- Direct writes to `main` require explicit instruction.
- This skill uploads experience only. It does not install or update the local global context.
