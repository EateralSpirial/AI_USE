---
name: evolve-user-agent-context
description: Evaluate strong execution feedback and evolve the user's global agent context. Use after resolving a difficult reusable problem, receiving material user dissatisfaction or correction, receiving durable workflow guidance, or when the user asks the agent to learn from an execution. Persist only high-confidence user-specific or cross-project experience; ask before contributing user-independent experience to AI_USE.
---

# Evolve User Agent Context

## Purpose

Turn selected execution experience into compact user-level onboarding for future agents. Apply a strict persistence threshold so the local global context gains durable judgment without accumulating routine task history.

## Strong Triggers

Evaluate experience when one of these events occurs:

- a difficult problem has been solved and its root cause or successful method is understood;
- the user expresses material dissatisfaction or gives a correction that reveals a durable expectation;
- the user provides a key instruction for a recurring workflow;
- the user explicitly asks the agent to retain or generalize a lesson.

A trigger starts evaluation. Persistence depends on the full acceptance test.

## Acceptance Test

Persist a candidate only when all relevant conditions hold:

- it is likely to improve decisions across future tasks;
- it carries meaningful rediscovery cost or protects a material boundary;
- the supporting evidence or user intent is clear;
- it can be expressed as a general trigger, principle or procedure, and expected effect;
- its scope is broader than the incident that revealed it;
- it adds distinct meaning beyond current local context;
- it can be recorded without secrets, sensitive data, or unnecessary project detail;
- the resulting guidance remains compact enough to justify its attention cost.

When evidence, durability, or scope remains weak, leave the candidate in task history.

## Classification

Classify every accepted candidate before editing context.

### 1. User-Specific Experience

Knowledge tied to this user's stable preferences, recurring environment, decision style, communication requirements, or cross-project workflow expectations.

Store it only in the user's local agent context.

### 2. General Cross-Project Experience

A technically grounded method, failure pattern, verification rule, or agent workflow that remains useful across projects and largely independent of this user's preferences.

Store it in the user's local context. It may also qualify for contribution to AI_USE.

Project architecture, project contracts, and project-local procedures belong in that project's context system. Routine implementation facts remain in code and direct evidence.

## Evolution Method

1. Reconstruct the trigger and separate observed evidence, user intent, and agent inference.
2. Form one concise candidate lesson and state its likely future trigger and effect.
3. Apply the acceptance test rigorously and classify the result.
4. Inspect the user's current global context for the narrowest canonical owner and for semantically overlapping guidance.
5. Extend or refine that owner. Create a new owner only when the lesson introduces a distinct reusable responsibility.
6. Express the accepted current meaning compactly. Preserve useful rationale and verification cues; let task history retain the incident narrative.
7. Check routes, remove stale parallel meanings, and review the result as a capable future agent.
8. Tell the user what was learned, where it was stored, and the scope assigned to it.

## User Corrections

Extract the durable operating expectation contained in the correction. Record the intended future behavior and the reason when it supports generalization. Preserve the user's exact wording only when the wording itself carries a stable requirement.

## Contribution to AI_USE

When an accepted lesson qualifies as general cross-project experience, explain briefly why it appears useful across users and projects, then ask the user whether to contribute it to AI_USE.

After explicit permission:

1. remove personal, private, machine-specific, and project-specific details;
2. inspect AI_USE principles, instructions, and skills to locate the narrowest canonical owner;
3. integrate the generalized meaning with the smallest coherent repository change;
4. preserve one canonical definition and update routes when needed;
5. verify the technical claim and review the final diff;
6. upload through the available GitHub workflow and report the resulting commit or pull request.

AI_USE receives only generalized user-independent experience. The user's local context remains the owner of personalized experience.
