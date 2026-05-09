# AI Workflow Knowledge Base

This is the working knowledge base inside GitHub Pattern Translator.

Its job is to turn scattered product updates, GitHub patterns, session lessons,
and user-specific practices into reusable operating guidance.

## Scope

Keep knowledge about:

- Codex workflow design
- subagent routing
- Chrome / Browser / Computer Use routing
- memory and handoff discipline
- skills and plugin design
- automations
- evidence-pack and verification workflows
- anti-patterns that caused failed runs

Do not use this file as a direct task implementation log. Worker sessions should
write their own status, evidence, and handoff files.

## Task Routing

Before execution, classify the task by its likely failure point:

- code understanding risk -> Context / Search plus Protocol Gate
- compact or session loss risk -> Memory plus Filesystem
- multi-role or long-task risk -> Harness / Orchestration
- unverified completion risk -> Verification / Evidence Pack
- browser/login risk -> Chrome
- local frontend/rendered-state risk -> Browser
- desktop app risk -> Computer Use
- repeated workflow risk -> Skill
- scheduled continuation risk -> Automation

## Pattern Translator Layers

Use only the layers needed for a task:

- Context / Search
- Memory
- Filesystem / Workspace
- Harness / Orchestration
- Protocol / Quality Gate
- Skill / Capability
- Browser / Sandbox
- Spec / Domain File
- Observability / Telemetry
- Verification / Evidence Pack

## Session Roles

Recommended split:

- Controller session: route, summarize, produce prompts, maintain knowledge,
  review handoffs, and decide next steps.
- Worker session: execute a scoped task and update evidence/handoff files.
- Subagent: bounded helper spawned from a controller session for parallel work.

Existing independent sessions are not centrally controllable by default. Use a
file control plane if they need coordination.

## Handoff Rule

Every long-running task should end with:

- current file paths
- completed items
- incomplete items
- validation commands run
- pass/fail status
- risks or blockers
- next open loops

If a conclusion matters after compact, put it in a durable file or sidecar
memory. Do not trust chat compact as the source of truth.

## Quality Gate

Never call work complete unless there is evidence:

- file diff or generated artifact
- command output
- test result
- CSV/report/checklist
- source citation
- screenshot/browser evidence when relevant

For high-risk tasks, separate:

- implementation result
- proxy evidence
- official evidence
- unresolved assumptions

## Repeatable Prompt

Use this when starting a new task from a controller session:

```text
This is a new task. Act as controller, not worker.

Output:
1. Task card
2. Pattern Translator layers to enable
3. Execution-session prompt
4. Acceptance criteria
5. Handoff format
6. Verification plan

Do not start implementation unless I explicitly ask.
```

## Local Skills Created From Patterns

### `$validate-quant-research`

Use when validating a quantitative strategy, factor, alpha claim, backtest,
portfolio rule, or research run before implementation or promotion.

Pattern origin:

- Evidence Pack
- Protocol / Quality Gate
- Observability / Telemetry
- Memory / Handoff

Core gate:

Do not call a result validated without config, data window, command, leakage
check, cost/execution assumptions, and artifact trail.
