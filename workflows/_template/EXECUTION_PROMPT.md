# Execution Prompt

Paste this into the worker session.

```text
Read these workflow files first:

- WORKFLOW.md
- TASK_CARD.md
- HANDOFF.md

You are the worker session. Execute only the scoped task in TASK_CARD.md.

Rules:
- Do not expand scope.
- Do not rely on chat memory as source of truth.
- Do not call work complete without evidence.
- Keep proxy evidence separate from official evidence.
- If requirements conflict, report the conflict with evidence before changing
  anything.

First action:
1. Restate the task goal in one sentence.
2. List the files/data you found.
3. Identify the highest-risk assumption.
4. Execute the next open loop from HANDOFF.md.

At the end of the turn, update HANDOFF.md with:
- Current paths
- Completed
- Not completed
- Commands run
- Artifacts produced
- Current pass/fail
- Known risks
- Next open loops
```
