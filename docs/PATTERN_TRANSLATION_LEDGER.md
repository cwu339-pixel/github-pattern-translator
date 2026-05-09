# Pattern Translation Ledger

This ledger stores optional GitHub pattern translations. It is not direct task
execution guidance.

## 2026-05-08 Hot-Scout

Scope:

- AI agent
- coding agent
- memory
- context
- workflow
- harness
- skill systems

Method:

- GitHub CLI search for recently created and recently active repos.
- Web search for ecosystem trend checks.
- Shallow translation only. No source audit unless separately requested.

Main signal:

The hot area is not "another agent framework". The hot area is the surrounding
operating system for agents:

- skills as reusable capability packages
- persistent memory and memory compilers
- context/search/knowledge graph layers
- browser and execution harnesses
- protocol enforcement
- virtual filesystems and file-backed context
- long-horizon task recovery

## Adopt Now

### Agent Context As Filesystem

Inspired by:

- `strukto-ai/mirage`
- `volcengine/OpenViking`
- `codejunkie99/agentic-stack`
- `openags/auto-research`

Local decision:

- Keep controller state in durable files.
- Keep role state under `agents/<role>/`.
- Keep protocol state under `docs/protocol/` or equivalent.
- Keep pattern research under `docs/patterns/` or equivalent.

Why:

This directly solves compact/session loss without depending on chat memory.

### Typed Session Memory

Inspired by:

- `coleam00/claude-memory-compiler`
- `thedotmack/claude-mem`
- `alash3al/stash`
- `mem0ai/mem0`

Local decision:

- Keep durable facts typed as constraints, decisions, state, and open loops.
- Promote only audited or explicitly requested facts.
- Do not let compact summaries become authoritative memory.

Why:

This prevents stale summaries from driving future work.

### Protocol Enforcement Gate

Inspired by:

- `GammaLabTechnologies/harmonist`
- `humanlayer/12-factor-agents`
- `emcie-co/parlant`

Local decision:

- Keep quality gates as real gates, not advisory notes.
- Important claims need local evidence, branch type, and source-card
  justification.
- Audit long trajectories regularly.

Why:

Many failed agent workflows fail from weak trajectory control, not from lack of
ideas.

## Adapt Next

### Codebase Knowledge Graph

Inspired by:

- `safishamsi/graphify`
- `MinishLab/semble`
- `topoteretes/cognee`

Local adaptation:

- Use index/graph/search output to propose source-card candidates.
- Verify by opening files and tests before using it for task prompts.
- Map results into route files only after confirmation.

Risk:

Graph hits can become keyword-chasing if the controller treats them as answers.

### Domain Files For Agents

Inspired by:

- `google-labs-code/design.md`
- `anthropics/skills`
- `obra/superpowers`

Local adaptation:

- Add domain files only after repeated ambiguity appears.
- Possible future files: `DOMAIN.md`, `QUALITY.md`, `ROUTE.md`.
- Keep these under protocol control and do not make them broad prompt dumps.

Risk:

Large context files can reduce judgment and increase generic behavior.

### Long-Horizon Harness

Inspired by:

- `karpathy/autoresearch`
- `bytedance/deer-flow`
- `langchain-ai/deepagents`

Local adaptation:

- Explorer agents can prepare in parallel.
- Main controller remains the owner of final sequence and judgment.
- Handoff unit is a source card, route node, or audit finding.

Risk:

Autonomy without gates recreates "AI answer -> keyword follow-up" drift.

## Watch

### Browser And Sandbox Harnesses

Repos:

- `browser-use/browser-harness`
- `TencentCloud/CubeSandbox`
- `h4ckf0r0day/obscura`

Why watch:

Useful for verification and isolated probes, but source and artifact evidence
should remain primary.

### Hermes/OpenClaw Ecosystem

Repos and signals:

- `NousResearch/hermes-agent`
- OpenClaw ecosystem
- `EKKOLearnAI/hermes-web-ui`
- `xaspx/hermes-control-interface`

Why watch:

Strong signal around agent control planes, persistent memory, skills,
multi-channel access, and status dashboards. Too much of the ecosystem is broad
autonomy or branding, so translate only narrow control-plane ideas.

## Reject For This Workspace

Reject by default:

- pure awesome lists
- prompt libraries with no operating model
- agent personality packs
- dashboards that do not improve evidence
- repos whose only value is "more tools"

Reason:

The typical failure mode is not lack of tools. It is weak evidence discipline
and overly linear prompt trajectories.
