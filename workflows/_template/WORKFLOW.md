# Workflow: <Name>

## Purpose

Describe what this workflow is for in one or two sentences.

## Use When

- The task has this shape:
- The main failure risk is:
- The work needs stable handoff across sessions:

## Do Not Use When

- The task is a one-off answer.
- The facts are not available.
- The workflow would add overhead without reducing risk.

## Pattern Translator Layers

Enable only the layers needed:

- [ ] Context / Search
- [ ] Memory
- [ ] Filesystem / Workspace
- [ ] Harness / Orchestration
- [ ] Protocol / Quality Gate
- [ ] Skill / Capability
- [ ] Browser / Sandbox
- [ ] Spec / Domain File
- [ ] Observability / Telemetry
- [ ] Verification / Evidence Pack

## Operating Pattern

```text
Signal:
Pattern:
State owner:
Handoff unit:
Recovery model:
Failure model:
Local translation:
Verdict:
```

## Execution Phases

1. Intake and scope
2. Evidence discovery
3. Risk and boundary check
4. Minimal execution or audit
5. Verification
6. Handoff

## Anti-Patterns

- Do not treat chat history as the source of truth.
- Do not expand scope because a related idea appeared.
- Do not call the task complete without evidence.
- Do not hide proxy evidence as official evidence.

## Acceptance Criteria

- [ ] The worker can execute from `EXECUTION_PROMPT.md` alone.
- [ ] `TASK_CARD.md` defines goal, sources, risks, and acceptance criteria.
- [ ] `HANDOFF.md` can restart the task after compact or session loss.
- [ ] Verification evidence is explicit.
