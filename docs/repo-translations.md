# Repo Translations

Hot-scout date: 2026-05-08.

Research depth: shallow GitHub metadata and public descriptions. These cards are
pattern translations, not source audits.

## Top Local Candidates

### `safishamsi/graphify`

- Signal: high-star new repo; turns code, schemas, scripts, docs, papers, images,
  and videos into a queryable knowledge graph.
- Pattern: codebase knowledge graph.
- State owner: graph index plus source artifact pointers.
- Handoff unit: query result with file/function/schema/document anchors.
- Recovery model: rebuild or refresh graph from filesystem.
- Failure model: graph can hallucinate importance if source is not reopened.
- Local translation: use graph/index output to propose source cards and route
  edges, then verify by opening files.
- Verdict: adapt.
- Confidence: medium.

### `MinishLab/semble`

- Signal: agent-focused code search claiming large token savings versus raw
  grep/read workflows.
- Pattern: token-budgeted source retrieval.
- State owner: code search index.
- Handoff unit: minimal relevant snippets and file anchors.
- Recovery model: re-query index after route branch changes.
- Failure model: high recall claims can hide missing call paths.
- Local translation: use search as a source-card candidate generator, not as the
  answer dependency.
- Verdict: adapt.
- Confidence: medium.

### `strukto-ai/mirage`

- Signal: unified virtual filesystem for AI agents.
- Pattern: agent context as filesystem.
- State owner: virtual filesystem namespace.
- Handoff unit: mounted file, context object, or namespace path.
- Recovery model: reconstruct context from durable filesystem state.
- Failure model: too many layers can obscure the real source of truth.
- Local translation: keep controller state explicit as files and role folders.
- Verdict: adopt pattern, not implementation.
- Confidence: medium.

### `dirac-run/dirac`

- Signal: coding agent focused on context curation, hash-anchored edits, parallel
  operations, and AST manipulation.
- Pattern: context curation plus anchored operations.
- State owner: curated context set and edit anchors.
- Handoff unit: hash-anchored source region or AST target.
- Recovery model: re-anchor to file hashes when context changes.
- Failure model: anchor machinery can become overkill for pure reading tasks.
- Local translation: use the anchoring idea for evidence cards: file path,
  symbol, local trigger, and reading event.
- Verdict: adapt.
- Confidence: low-medium.

### `coleam00/claude-memory-compiler`

- Signal: captures Claude Code sessions and compiles them into structured,
  cross-referenced knowledge articles.
- Pattern: session memory compiler.
- State owner: compiler output knowledge base.
- Handoff unit: promoted decision, lesson, source reference, or article.
- Recovery model: rehydrate future sessions from compiled memory.
- Failure model: compiled memory can preserve wrong conclusions.
- Local translation: keep durable facts narrow, typed, and auditable.
- Verdict: adapt.
- Confidence: medium.

### `google-labs-code/design.md`

- Signal: format spec for persistent design-system understanding by coding
  agents.
- Pattern: domain facts as agent-readable files.
- State owner: `DESIGN.md`.
- Handoff unit: stable design rule, token, component convention, or constraint.
- Recovery model: reload the file in future coding sessions.
- Failure model: stale design docs can override current product reality.
- Local translation: use the same idea for domain, route, or quality files only
  when repeated ambiguity appears.
- Verdict: adapt.
- Confidence: high.

### `browser-use/browser-harness`

- Signal: self-healing browser harness for LLM task execution.
- Pattern: recoverable browser control layer.
- State owner: browser task/session controller.
- Handoff unit: browser state, action result, screenshot, or DOM evidence.
- Recovery model: self-heal selectors/actions after page changes.
- Failure model: browser success can hide source-level misunderstanding.
- Local translation: use browser evidence for UI verification, never as a
  replacement for source anchors.
- Verdict: watch/adapt.
- Confidence: medium.

### `TencentCloud/CubeSandbox`

- Signal: concurrent secure lightweight sandbox for AI agents.
- Pattern: bounded execution environment.
- State owner: sandbox instance plus permission profile.
- Handoff unit: command result, artifact, or isolated workspace.
- Recovery model: recreate sandbox from clean baseline.
- Failure model: sandbox limits can be mistaken for project failures.
- Local translation: useful when probes need isolated execution.
- Verdict: watch.
- Confidence: medium.

### `GammaLabTechnologies/harmonist`

- Signal: portable orchestration with mechanical protocol enforcement.
- Pattern: protocol enforcement agent.
- State owner: protocol definition and agent status.
- Handoff unit: validated status, directive, or compliance result.
- Recovery model: resume from protocol state rather than chat history.
- Failure model: mechanical compliance can become performative if evidence is
  weak.
- Local translation: strengthen quality gates around evidence completeness,
  branch type, and audit cadence.
- Verdict: adapt.
- Confidence: medium.

### `sandeco/reversa`

- Signal: transforms legacy systems into executable specifications for coding
  agents.
- Pattern: legacy-to-spec compiler.
- State owner: executable spec or behavior map.
- Handoff unit: behavior rule, invariant, or generated spec case.
- Recovery model: regenerate spec from source when implementation changes.
- Failure model: spec can look precise while missing runtime edge cases.
- Local translation: convert findings into route/source cards, not polished
  generalized docs.
- Verdict: adapt.
- Confidence: medium.

## Ecosystem Signals

These are important trend signals but should not be copied directly.

### `NousResearch/hermes-agent`

- Pattern: persistent agent that grows through memory, skills, and integrations.
- Local translation: useful as a reminder that growth needs permission gates,
  memory hygiene, and status visibility.
- Verdict: watch.

### OpenClaw ecosystem

- Pattern: local/self-hosted agent harness with skills, messaging, memory, and
  broad tool access.
- Local translation: borrow the control-plane idea, not broad autonomy.
- Verdict: watch.

### `obra/superpowers`

- Pattern: skills as software-development methodology.
- Local translation: turn repeated high-value workflows into small skills only
  after they are proven.
- Verdict: adapt.

### `affaan-m/everything-claude-code`

- Pattern: full harness pack for skills, memory, security, and performance.
- Local translation: useful inventory, but likely too broad for default context.
- Verdict: watch.

### `anthropics/skills`

- Pattern: standardized skill packages.
- Local translation: validates the skill-as-capability direction.
- Verdict: adapt.

### `karpathy/autoresearch`

- Pattern: long-running research loop with autonomous experiments.
- Local translation: useful for long-horizon recovery, but keep it constrained
  by evidence and explicit review.
- Verdict: adapt carefully.

### `bytedance/deer-flow`

- Pattern: long-horizon harness with sandboxes, memories, tools, skills,
  subagents, and gateway.
- Local translation: borrow coordinator/subagent boundaries and recoverable
  handoffs.
- Verdict: adapt.

### `langchain-ai/deepagents`

- Pattern: planning tool, filesystem backend, and subagent spawning.
- Local translation: validates filesystem-backed work plus explicit delegation.
- Verdict: adapt.
