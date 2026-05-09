# Execution Prompt

Paste this into the worker session.

```text
Read these workflow files first:

- workflows/activation-layer-v0/WORKFLOW.md
- workflows/activation-layer-v0/TASK_CARD.md
- workflows/activation-layer-v0/HANDOFF.md

You are the worker session. Execute only Activation Layer v0.

Rules:
- Do not expand scope into automatic GitHub repo translation.
- Do not add network calls, model calls, or dependencies.
- Do not stage or publish private local execution-pack files.
- Do not overwrite existing workflows by default.
- Do not call work complete without running the verification commands.

First action:
1. Restate the task goal in one sentence.
2. List the files/data you found.
3. Identify the highest-risk assumption.
4. Execute the next open loop from HANDOFF.md.

At the end of the turn, update workflows/activation-layer-v0/HANDOFF.md with:
- Current paths
- Completed
- Not completed
- Commands run
- Artifacts produced
- Current pass/fail
- Known risks
- Next open loops
```
