# Translator Protocol

## Hot-Scout Prompt

Use this when scouting GitHub or product updates:

```text
Run a hot-scout for AI agent, coding agent, memory, context, workflow, harness,
and skill projects.

Use a recent window first: created or substantially active in the last 30-45
days. Do not rank by stars alone. Consider created date, pushed date, stars,
forks, README specificity, whether the repo contains real code or only
marketing, and whether the idea can be translated into a file-driven agent OS.

Output:
1. 20 candidates grouped by pattern.
2. The core operating pattern for each repo.
3. State owner, handoff unit, recovery model, and failure model.
4. Verdict: adopt, adapt, watch, or reject.
5. Top 5 changes worth writing into the Pattern Translator.
```

## After Translation

If the translated pattern will be executed by a worker session or reused later,
materialize it into:

```text
workflows/<workflow-name>/
  WORKFLOW.md
  TASK_CARD.md
  EXECUTION_PROMPT.md
  HANDOFF.md
```

Use `workflows/_template/` as the starting point.

## Translation Card

Every repo card should use this shape:

```text
Repo:
Signal:
Pattern:
State owner:
Handoff unit:
Recovery model:
Failure model:
Local translation:
Verdict:
Confidence:
```

## Scoring

Use this 0-2 scoring pass before a repo enters the ledger:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Recent signal | old or inactive | active but not new | newly hot or recently active |
| Substance | list/marketing | partial code or examples | runnable code, tests, concrete docs |
| Pattern clarity | vague | has one useful idea | has a transferable operating model |
| Fit | unrelated | indirect | directly helps source, memory, route, audit, or recovery |
| Risk | likely hype or unsafe | unknown | bounded and easy to adapt |

Decision:

- `adopt`: can be encoded as a local rule or file now.
- `adapt`: useful idea, but needs a local version.
- `watch`: high signal, not enough confidence.
- `reject`: not relevant, too broad, unsafe, or mostly hype.

## Guardrails

- Mark shallow metadata research as shallow. Do not pretend it is source review.
- Prefer patterns over product claims.
- Treat sudden star spikes as discovery signals, not proof.
- Keep the Pattern Translator separate from task execution.
- If a pattern affects real work, pass it through the local evidence gate first.
