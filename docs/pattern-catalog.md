# Pattern Catalog

These are patterns, not endorsements of the repos that inspired them.

## P1: Codebase Knowledge Graph

External signal:

- `safishamsi/graphify`
- `MinishLab/semble`
- `topoteretes/cognee`

Operating idea:

Turn code, schemas, docs, tests, and runtime notes into a queryable graph or
indexed map before spending large context on raw file reads.

Local translation:

- Generate source-card candidates from file/function/test relationships.
- Let route files own route nodes and edges.
- Use graph/index hits as reading triggers, not final evidence.

Failure to avoid:

- treating graph output as ground truth without opening the source file
- replacing route judgment with keyword search

Verdict: adapt.

## P2: Session Memory Compiler

External signal:

- `coleam00/claude-memory-compiler`
- `thedotmack/claude-mem`
- `alash3al/stash`
- `mem0ai/mem0`

Operating idea:

Capture session events, compress them into durable facts, and re-inject only the
facts needed for the next session.

Local translation:

- Keep durable memory split into constraints, decisions, state, and open loops.
- Promote facts only when they survive an audit or explicit user instruction.
- Keep compact summaries as cache, not memory.

Failure to avoid:

- storing everything
- re-injecting stale or unverified claims
- letting prior assistant summaries outrank source files

Verdict: adopt the shape, keep implementation local.

## P3: Virtual Filesystem For Agent Context

External signal:

- `strukto-ai/mirage`
- `volcengine/OpenViking`
- `codejunkie99/agentic-stack`

Operating idea:

Represent agent context as a portable filesystem: memory, skills, protocols,
artifacts, and session state are explicit files instead of hidden chat state.

Local translation:

- Keep each role under `agents/<role>/`.
- Keep durable protocol state under `docs/protocol/`.
- Keep optional research under `docs/patterns/` or equivalent.

Failure to avoid:

- duplicating state across many files without a source of truth
- letting optional pattern notes leak into task execution

Verdict: adopt.

## P4: Protocol Enforcement Agent

External signal:

- `GammaLabTechnologies/harmonist`
- `humanlayer/12-factor-agents`
- `emcie-co/parlant`

Operating idea:

Make protocol compliance mechanical: define allowed transitions, required
fields, quality gates, and stop conditions.

Local translation:

- Require source-card completeness and style-risk checks.
- Require branch type, reading event, and local trigger for evidence-heavy work.
- Run audits on long trajectories.

Failure to avoid:

- relying on "the agent should know" instead of explicit gates
- turning the gate into a checklist with no judgment

Verdict: adapt.

## P5: Long-Horizon Harness

External signal:

- `bytedance/deer-flow`
- `karpathy/autoresearch`
- `langchain-ai/deepagents`

Operating idea:

Long tasks need durable plans, isolated workspaces, tool boundaries, and
recoverable handoffs between subagents.

Local translation:

- Reader or explorer agents may prepare evidence in parallel.
- Main controller owns final sequencing and judgment.
- Handoff unit is a source card, route node, or audit result, not a freeform
  chat summary.

Failure to avoid:

- letting subagents control final decisions
- pre-generating fixed scripts for dynamic work
- accepting long-running autonomy without audits

Verdict: adapt.

## P6: Skill As Capability Package

External signal:

- `anthropics/skills`
- `obra/superpowers`
- `google/agents-cli`
- `iamzhihuix/skills-manage`

Operating idea:

Package a workflow as instructions plus optional resources and scripts, then
load it only when the task matches.

Local translation:

- Keep skills narrow and trigger-based.
- Prefer local project rules before general skills.
- Convert repeated controller actions into small skills only after they
  stabilize.

Failure to avoid:

- kitchen-sink skills that consume context before the task is clear
- installing skills because they are popular rather than needed

Verdict: adapt.

## P7: Browser And Sandbox Harness

External signal:

- `browser-use/browser-harness`
- `TencentCloud/CubeSandbox`
- `h4ckf0r0day/obscura`

Operating idea:

Agents need controlled execution environments for web tasks, local tests, and
tool side effects.

Local translation:

- Use browser/sandbox tooling for verification, not as source of truth.
- Keep destructive and externally visible actions behind explicit approval.
- For code work, probes are evidence only when cheap and bounded.

Failure to avoid:

- allowing broad autonomous browser exploration
- treating generated observations as understanding without source anchors

Verdict: watch/adapt.

## P8: Legacy-To-Spec Compiler

External signal:

- `sandeco/reversa`
- `google-labs-code/design.md`

Operating idea:

Turn implicit behavior into explicit, executable or agent-readable specs.

Local translation:

- Convert code-reading findings into route cards, not polished tutorials.
- Add domain files only if they reduce repeated ambiguity.
- For UI/design work, make persistent design facts explicit before prompting.

Failure to avoid:

- writing specs that are prettier than they are true
- treating generated specs as a substitute for tests or source references

Verdict: adapt.

## P9: Observability / Telemetry

External signal:

- `getagentseal/codeburn`
- token/session trackers

Operating idea:

Measure where agent time, tokens, retries, failures, and context churn happen.

Local translation:

- Keep turn ledgers for long workflows.
- Track commands, artifacts, pass/fail state, and open loops.
- Use telemetry to improve routing and skills, not to optimize for activity.

Failure to avoid:

- confusing more activity with more progress
- hiding failed attempts because only the final run looked good

Verdict: adapt.

## P10: Verification / Evidence Pack

External signal:

- research harnesses
- evaluation frameworks
- incident and telemetry workflows

Operating idea:

Every claim should map to artifacts: config, command, output, report, checklist,
or source citation.

Local translation:

- Separate proxy evidence from official evidence.
- Make acceptance criteria explicit.
- End long work with a handoff and open loops.

Failure to avoid:

- saying "done" without reproducing the result
- generating a polished report with no command trail

Verdict: adopt.

## P11: Workflow Materialization

External signal:

- file-backed agent workspaces
- long-running subagent workflows
- durable handoff systems

Operating idea:

Translated patterns should become executable file bundles before a worker starts.

Local translation:

- `WORKFLOW.md` owns the reusable pattern.
- `TASK_CARD.md` owns the current task facts and acceptance criteria.
- `EXECUTION_PROMPT.md` owns the worker instructions.
- `HANDOFF.md` owns recovery state and next open loops.

Failure to avoid:

- leaving the translated pattern in chat only
- restarting from memory after compact
- letting worker sessions expand scope from adjacent questions

Verdict: adopt.
