# Workflow: Auto Research Brief

## Purpose

Turn a broad "research this" request into a scoped, evidence-backed brief that
can survive session drift, compacting, and handoff to another worker.

## Use When

- The task asks for current or niche information from web, GitHub, docs, APIs,
  or user-provided project material.
- The main failure risk is unsupported synthesis, stale sources, or confusing
  proxy evidence with official evidence.
- The work needs stable handoff across sessions because research can branch and
  the final answer must still trace back to sources.

## Do Not Use When

- The task is a one-off answer that can be handled directly.
- The user explicitly says not to browse or not to do research.
- The research question is so vague that no useful source plan can be formed.
- The workflow would add overhead without reducing risk.

## Pattern Translator Layers

Enable only the layers needed:

- [x] Context / Search
- [x] Memory
- [ ] Filesystem / Workspace
- [ ] Harness / Orchestration
- [x] Protocol / Quality Gate
- [ ] Skill / Capability
- [x] Browser / Sandbox
- [ ] Spec / Domain File
- [ ] Observability / Telemetry
- [x] Verification / Evidence Pack

## Operating Pattern

```text
Signal: "research this", "latest", "what is popular", "compare these repos", or "how do people use this"
Pattern: scope question -> source plan -> evidence ledger -> claim ledger -> synthesis -> handoff
State owner: workflow files plus HANDOFF.md, not chat memory
Handoff unit: scoped question, searched sources, supported claims, unresolved gaps, next loops
Recovery model: restart from HANDOFF.md and rerun only missing source/evidence loops
Failure model: broad wandering research, stale facts, weak citations, or claims not tied to evidence
Local translation: make the smallest source-backed brief that answers the user's actual decision
Verdict: use for ambiguous research; skip for simple facts or implementation-only coding tasks
```

## Execution Phases

1. Intake and scope
2. Source plan
3. Evidence discovery
4. Claim ledger
5. Synthesis
6. Verification and handoff

## Anti-Patterns

- Do not treat chat history as the source of truth.
- Do not expand scope because a related idea appeared.
- Do not call the task complete without evidence.
- Do not hide proxy evidence as official evidence.
- Do not report "latest" unless sources were checked during the task.
- Do not turn popularity signals into product truth without caveats.

## Acceptance Criteria

- [x] The worker can execute from `EXECUTION_PROMPT.md` alone.
- [x] `TASK_CARD.md` defines goal, sources, risks, and acceptance criteria.
- [x] `HANDOFF.md` can restart the task after compact or session loss.
- [x] Verification evidence is explicit.
