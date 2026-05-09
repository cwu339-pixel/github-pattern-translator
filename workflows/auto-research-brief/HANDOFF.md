# Handoff: Auto Research Brief

## Current Paths

- Workflow: `workflows/auto-research-brief/`
- Template source: `workflows/_template/`
- Activation scripts: `scripts/init_workflow.py`, `scripts/render_worker_prompt.py`, `scripts/check_handoff.py`

## Completed

- [x] Initialized the workflow with `scripts/init_workflow.py auto-research-brief`.
- [x] Filled `WORKFLOW.md` with the operating pattern and quality gates.
- [x] Filled `TASK_CARD.md` with deliverables, risks, and acceptance criteria.
- [x] Filled `EXECUTION_PROMPT.md` with a worker-ready research protocol.
- [x] Filled this handoff with recovery state.
- [x] Rendered the worker prompt successfully.
- [x] Checked handoff completeness successfully.

## Not Completed

- [ ] Decide whether to commit/push this practice workflow.
- [ ] Use the workflow on a live external research question.

## Commands Run

```bash
git status --short
find workflows -maxdepth 2 -type f | sort
sed -n '1,220p' workflows/_template/WORKFLOW.md
sed -n '1,220p' workflows/_template/TASK_CARD.md
python scripts/init_workflow.py auto-research-brief
python scripts/render_worker_prompt.py workflows/auto-research-brief
python scripts/check_handoff.py workflows/auto-research-brief
```

## Artifacts Produced

- `workflows/auto-research-brief/WORKFLOW.md`
- `workflows/auto-research-brief/TASK_CARD.md`
- `workflows/auto-research-brief/EXECUTION_PROMPT.md`
- `workflows/auto-research-brief/HANDOFF.md`

## Current Pass/Fail

- Status: pass
- Reason: the workflow renders into a worker-ready prompt and its handoff passes completeness checks
- Evidence: `render_worker_prompt.py` produced the expected prompt; `check_handoff.py` exited 0

## Known Risks

- This is a reusable research workflow, not evidence for any particular external topic.
- Over-broad research can still drift unless the worker scopes the user's decision first.
- Current repo has unrelated local changes outside this workflow; do not stage them with this task.

## Next Open Loops

1. Scan candidate files for private local strings before publishing.
2. If clean, commit only this workflow directory.
3. Use the workflow on a live external research question.

## Notes For Next Session

Continue only the open loops above. Do not touch unrelated local changes in
`README.md`, `docs/PATTERN_TRANSLATION_LEDGER.md`, or
`docs/ai-decision-card-execution-pack.md`.
