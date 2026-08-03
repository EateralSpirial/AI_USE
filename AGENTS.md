# Model Selection for Subagents, Multi-Agent Workflows, and Codex Tasks

Use the least expensive model that can **reliably complete and verify** the task. Select models based on uncertainty, verification difficulty, and the cost of error.

## Models

* **Luna (`gpt-5.6-luna`)**: Use for tasks with clear objectives, bounded scope, and practical verification. Suitable for retrieval, summarization, codebase inspection, mechanical edits, deterministic implementation, and most well-defined coding tasks. Use **max** thinking effort for complex but well-specified work.

* **Sol (`gpt-5.6-sol`)**: Use for open-ended work, incomplete or conflicting evidence, novel architecture, difficult debugging, hard-to-verify results, or high-cost mistakes. **Medium** effort is often sufficient for short Sol tasks and may offer better value than using a weaker model tier.

## Sol Reasoning Effort

* **medium**: Short or focused tasks requiring Sol-level judgment.
* **high**: Default for substantial open-ended work.
* **xhigh**: Long dependency chains, large changes, or complex multi-step work.
* **max**: Reserve for Luna to execute difficult and certain tasks.
* **ultra/max**: Reserve for Sol to solve the most difficult tasks with exceptional reasoning demands.

Start with the lowest suitable model and reasoning effort. Escalate when the agent cannot form a confident plan, evidence conflicts, an attempt fails without a clear cause, or correctness remains difficult to verify.

## User-Level Context Evolution

After resolving a difficult reusable problem, receiving a material user correction, or receiving durable workflow guidance, use `evolve-user-agent-context` to evaluate whether the lesson belongs in the user's global agent context. Apply a strict threshold, update the narrowest canonical local owner, and ask before contributing user-independent experience to AI_USE.
