# Task Card: Activation Layer v0

## Task Goal

Add the smallest useful setup layer for GitHub Pattern Translator so a user can
materialize a translated pattern into workflow files, send a stable worker
prompt, and check handoff completeness.

## Final Deliverables

- `scripts/init_workflow.py`
- `scripts/render_worker_prompt.py`
- `scripts/check_handoff.py`
- README Quickstart for the activation layer
- Updated workflow documentation if needed
- Updated `workflows/activation-layer-v0/HANDOFF.md`

## Fact Sources

- Code: current repository files
- Local data: `workflows/_template/`
- Web/GitHub: not required for v0
- API docs: not required for v0
- User-provided context: need setup so patterns are actually usable
- Run results: local script validation
- Tests: script `--help`, temporary workflow creation, render, and handoff check

## Max Risks

- [x] Misunderstanding the requirement
- [x] Losing state after compact/session switch
- [ ] Multi-agent drift
- [x] Claiming completion without verification
- [x] Editing the wrong files
- [x] Treating proxy evidence as official evidence
- [x] Publishing private local project context

## Task Length

- [ ] One pass
- [x] Multi-turn
- [ ] Long task

## Handoff Required

- [x] Yes
- [ ] No

## Acceptance Criteria

- [x] `init_workflow.py` copies `_template` into `workflows/<name>` and refuses
      to overwrite existing workflows unless explicitly forced.
- [x] `render_worker_prompt.py` prints a worker prompt containing the workflow,
      task card, and current handoff context.
- [x] `check_handoff.py` reports missing required handoff sections or empty
      placeholders.
- [x] Scripts work from the repo root without installation.
- [x] Scripts provide useful `--help`.
- [x] Validation commands are recorded in `HANDOFF.md`.
- [x] Public changes exclude private local execution-pack files.

## Forbidden Actions

- Do not implement automatic GitHub repo analysis in v0.
- Do not add API keys, model calls, or network dependencies.
- Do not stage or publish local private execution-pack files.
- Do not overwrite user-created workflows by default.

## Verification Commands

```bash
python scripts/init_workflow.py --help
python scripts/render_worker_prompt.py --help
python scripts/check_handoff.py --help
python scripts/init_workflow.py dogfood-smoke --output-dir /tmp/gpt-workflows
python scripts/render_worker_prompt.py /tmp/gpt-workflows/dogfood-smoke
python scripts/check_handoff.py /tmp/gpt-workflows/dogfood-smoke
```

## Current Status

- Status: implemented and locally verified
- Last updated: 2026-05-09
- Current owner/session: GitHub Pattern Translator
