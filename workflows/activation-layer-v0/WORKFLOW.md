# Workflow: Activation Layer v0

## Purpose

Turn GitHub Pattern Translator from a documentation repo into a usable workflow
materialization kit. Keep the first activation layer small: initialize workflow
folders, render worker prompts, and check handoff completeness.

## Use When

- The repo already has translated patterns and workflow templates.
- The main failure risk is that users read the docs but do not know how to
  start or keep worker sessions anchored.
- The work needs stable handoff across sessions and should avoid chat-only
  execution state.

## Do Not Use When

- The goal is to build an automatic GitHub repo analyzer.
- The goal is to manage live worker sessions directly.
- The workflow would add a complex CLI before the file protocol is proven.

## Pattern Translator Layers

- [ ] Context / Search
- [ ] Memory
- [x] Filesystem / Workspace
- [ ] Harness / Orchestration
- [x] Protocol / Quality Gate
- [x] Skill / Capability
- [ ] Browser / Sandbox
- [ ] Spec / Domain File
- [x] Observability / Telemetry
- [x] Verification / Evidence Pack

## Operating Pattern

```text
Signal:
The repo has useful translation docs and workflow templates, but users still
need a setup path to materialize and execute translated patterns.

Pattern:
Workflow Materialization Kit.

State owner:
workflows/<workflow-name>/ with WORKFLOW.md, TASK_CARD.md,
EXECUTION_PROMPT.md, and HANDOFF.md.

Handoff unit:
A rendered worker prompt plus HANDOFF.md.

Recovery model:
Next session reads HANDOFF.md and continues only the listed open loops.

Failure model:
Overbuilding an AI-powered CLI, publishing private local context, or letting
worker sessions expand scope from adjacent questions.

Local translation:
Add three deterministic scripts and Quickstart docs. No API calls, no automatic
repo translation, no session control.

Verdict:
Adopt as v0 activation layer.
```

## Execution Phases

1. Create this dogfood workflow.
2. Confirm that scope is limited to deterministic file operations.
3. Add `scripts/init_workflow.py`.
4. Add `scripts/render_worker_prompt.py`.
5. Add `scripts/check_handoff.py`.
6. Update README and workflow docs with Quickstart.
7. Validate with a temporary workflow.
8. Update `HANDOFF.md`.

## Anti-Patterns

- Do not build `translate <repo>` in v0.
- Do not add network calls or model calls.
- Do not publish local/private project execution packs.
- Do not require installation before the scripts are useful.
- Do not hide incomplete handoff fields.

## Acceptance Criteria

- [ ] A user can run `python scripts/init_workflow.py <name>`.
- [ ] A user can render a copy-paste worker prompt from a workflow folder.
- [ ] A user can check whether `HANDOFF.md` has required fields populated.
- [ ] Scripts have `--help`.
- [ ] Validation uses a temporary workflow and does not modify private files.
- [ ] README explains the v0 Quickstart.
