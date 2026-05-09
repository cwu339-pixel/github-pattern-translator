# GitHub Pattern Translator

GitHub Pattern Translator turns hot GitHub/Codex/agent workflow ideas into
local, reusable operating patterns.

It is not a leaderboard and it is not an agent framework. It is a translation
layer:

```text
repo or product signal -> operating pattern -> local workflow -> reusable skill or playbook
```

## What It Captures

- state ownership
- handoff units
- recovery models
- failure modes
- quality gates
- evidence requirements
- reusable task-routing templates
- anti-patterns that make agent workflows drift

## Why It Exists

Most agent projects advertise tools, autonomy, memory, or orchestration. The
useful part is often smaller:

- a way to persist context
- a clean handoff artifact
- a validation gate
- a strategy for long-horizon recovery
- a pattern for packaging repeatable work as a skill

This repo extracts those reusable parts and rewrites them as practical workflow
cards.

## Core Documents

- [AI workflow knowledge base](docs/AI_WORKFLOW_KB.md)
- [Translator protocol](docs/translator-protocol.md)
- [Pattern catalog](docs/pattern-catalog.md)
- [Repo translations](docs/repo-translations.md)
- [Pattern translation ledger](docs/PATTERN_TRANSLATION_LEDGER.md)

## Example Skill

- [`validate-quant-research`](skills/validate-quant-research/SKILL.md): a
  pattern-derived skill for auditing quantitative strategies, factors, alpha
  claims, and backtests before implementation or promotion.

## Basic Workflow

1. Scout a repo, tool, product update, or workflow idea.
2. Ignore popularity until the operating model is clear.
3. Translate it into a card:

```text
Pattern:
State owner:
Handoff unit:
Recovery model:
Failure model:
Local translation:
Verdict:
Confidence:
```

4. Decide whether to adopt, adapt, watch, or reject.
5. Promote stable repeated workflows into skills or playbooks.

## Non-Goals

- Do not copy external agent frameworks wholesale.
- Do not treat star count as proof.
- Do not use this as a substitute for source reading, testing, or validation.
- Do not let workflow patterns override project-specific constraints.
