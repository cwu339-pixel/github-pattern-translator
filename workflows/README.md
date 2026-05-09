# Workflows

This directory is the execution layer of GitHub Pattern Translator.

Use it after a pattern has been translated and you want a worker session,
subagent, or future thread to execute without drifting.

## Flow

```text
Translate -> Materialize -> Execute -> Handoff -> Re-anchor
```

## Directory Shape

Create one workflow folder per reusable execution pattern:

```text
workflows/<workflow-name>/
  WORKFLOW.md
  TASK_CARD.md
  EXECUTION_PROMPT.md
  HANDOFF.md
```

Use `workflows/_template/` as the starting point.

## Quickstart

From the repository root:

```bash
python scripts/init_workflow.py auto-research-breakdown
python scripts/render_worker_prompt.py workflows/auto-research-breakdown
python scripts/check_handoff.py workflows/auto-research-breakdown
```

`init_workflow.py` creates a workflow from `workflows/_template/` and refuses
to overwrite an existing workflow unless `--force` is provided.

`render_worker_prompt.py` prints a copy-paste prompt for a worker session,
including the execution prompt, task card, workflow, and current handoff state.

`check_handoff.py` exits nonzero while required handoff sections are missing or
still placeholder-only. That is expected for a newly initialized workflow; run it
again after the worker updates `HANDOFF.md`.

## Responsibilities

### Translator Session

- turns an external repo/product/update into a workflow
- writes or updates the workflow files
- defines acceptance criteria and anti-patterns
- reviews worker handoffs

### Worker Session

- reads `EXECUTION_PROMPT.md`
- executes only the scoped task
- updates `HANDOFF.md`
- does not expand scope unless the translator/user approves

## Re-Anchor Prompt

When a worker session starts drifting, paste:

```text
Re-anchor to the workflow files.

Read:
- WORKFLOW.md
- TASK_CARD.md
- EXECUTION_PROMPT.md
- HANDOFF.md

Continue only the Next open loops. Do not expand scope.
```

## Promotion Rule

A translated pattern should become a workflow when it will be reused or when the
task is long enough that chat memory is likely to drift.

A workflow should become a skill only after the workflow has stabilized across
real use.
