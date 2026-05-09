# Handoff: Activation Layer v0

## Current Paths

- Workflow: `workflows/activation-layer-v0/`
- Templates: `workflows/_template/`
- Scripts: `scripts/init_workflow.py`, `scripts/render_worker_prompt.py`, `scripts/check_handoff.py`
- Public docs touched in this task: `workflows/README.md`
- Public docs intentionally not touched in this task: `README.md`, `docs/PATTERN_TRANSLATION_LEDGER.md`, `docs/ai-decision-card-execution-pack.md`

## Completed

- [x] Scoped activation layer to deterministic file operations.
- [x] Created workflow files for dogfooding the repo's own execution protocol.
- [x] Implemented `scripts/init_workflow.py`.
- [x] Implemented `scripts/render_worker_prompt.py`.
- [x] Implemented `scripts/check_handoff.py`.
- [x] Added activation-layer Quickstart to `workflows/README.md`.
- [x] Ran local verification commands.
- [x] Confirmed public candidate files do not contain private local project paths.

## Not Completed

- [ ] Decide whether to commit/push only the public-safe activation-layer files.
- [ ] Consider whether this should be promoted into a Codex skill after more real use.

## Commands Run

```bash
git status --short
find workflows -maxdepth 3 -type f | sort
sed -n '1,180p' workflows/_template/WORKFLOW.md
sed -n '1,180p' workflows/_template/TASK_CARD.md
sed -n '1,180p' workflows/_template/EXECUTION_PROMPT.md
sed -n '1,180p' workflows/_template/HANDOFF.md
python scripts/init_workflow.py --help
python scripts/render_worker_prompt.py --help
python scripts/check_handoff.py --help
rm -rf /tmp/gpt-workflows
python scripts/init_workflow.py dogfood-smoke --output-dir /tmp/gpt-workflows
python scripts/init_workflow.py dogfood-smoke --output-dir /tmp/gpt-workflows
python scripts/render_worker_prompt.py /tmp/gpt-workflows/dogfood-smoke
python scripts/check_handoff.py /tmp/gpt-workflows/dogfood-smoke
python scripts/check_handoff.py workflows/activation-layer-v0
# private-string scan against public candidate files with a local denylist
python -m py_compile scripts/init_workflow.py scripts/render_worker_prompt.py scripts/check_handoff.py
git diff --check -- workflows/README.md
```

Result:

```text
Template shape confirmed. The three scripts initialize workflows, render worker
prompts, and check handoff completeness from the repo root. Fresh template
handoff correctly fails completeness checks until populated. The activation
workflow handoff passes completeness checks after this update. Re-running
`init_workflow.py` against an existing target exits nonzero unless `--force` is
provided. The public candidate files contain no matching private path/project
strings. The scripts compile under Python, and the tracked README diff has no
whitespace errors.
```

## Artifacts Produced

- `workflows/activation-layer-v0/WORKFLOW.md`
- `workflows/activation-layer-v0/TASK_CARD.md`
- `workflows/activation-layer-v0/EXECUTION_PROMPT.md`
- `workflows/activation-layer-v0/HANDOFF.md`
- `scripts/init_workflow.py`
- `scripts/render_worker_prompt.py`
- `scripts/check_handoff.py`
- `workflows/README.md`

## Current Pass/Fail

- Status: pass
- Reason: activation-layer v0 is implemented, locally verified, and scoped to deterministic file operations
- Evidence: help output, temporary workflow creation, worker prompt rendering, expected template handoff failure, activation handoff pass, and private-string scan

## Known Risks

- Local repo has unrelated private execution-pack changes.
- A large CLI would overfit before the file protocol is proven.
- Root `README.md` remains locally modified outside this task; do not stage it without reviewing those unrelated changes.

## Next Open Loops

1. Decide whether to commit/push only the activation-layer files.
2. Use this workflow on one external GitHub pattern translation.
3. If it survives reuse, promote the stable protocol into a Codex skill.

## Notes For Next Session

Start by reading this file, then continue only the open loops above. Do not
stage `README.md`, `docs/PATTERN_TRANSLATION_LEDGER.md`, or
`docs/ai-decision-card-execution-pack.md` unless the user explicitly asks to
publish those unrelated local changes.
