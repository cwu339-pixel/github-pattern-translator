# Task Card: Auto Research Brief

## Task Goal

Given a user research question, produce a concise brief whose claims are tied to
current, inspectable sources, then leave a handoff that another session can
continue without relying on chat memory.

## Final Deliverables

- Research brief: final answer or `research_brief.md` when the task needs a file
- Evidence ledger: source, date checked, source type, and what it supports
- Claim ledger: important claims mapped to evidence or marked as unresolved
- Decision: what the user should do next, with confidence and caveats
- Handoff: updated `HANDOFF.md`

## Fact Sources

- Code: repository files when the research concerns a local or GitHub project
- Local data: user-provided docs, dumps, notes, or previous outputs
- Web/GitHub: official docs, repos, releases, issues, discussions, and primary sources
- API docs: official API documentation for product/platform behavior
- User-provided context: the user's goal, constraints, domain, and examples
- Run results: commands, browser checks, local reproduction, or data inspection
- Tests: source cross-checks, date checks, and claim-to-source review

## Max Risks

- [x] Misunderstanding the requirement
- [x] Losing state after compact/session switch
- [x] Multi-agent drift
- [x] Claiming completion without verification
- [x] Editing the wrong files
- [x] Treating proxy evidence as official evidence
- [x] Over-browsing broad topics without answering the user's decision

## Task Length

- [ ] One pass
- [x] Multi-turn
- [ ] Long task

## Handoff Required

- [x] Yes
- [ ] No

## Acceptance Criteria

- [x] Research question is scoped before broad source gathering.
- [x] Current or unstable facts are verified during the task.
- [x] Each major claim is supported by a source or explicitly marked as unresolved.
- [x] Official/primary sources are separated from community or proxy evidence.
- [x] Final answer includes a practical recommendation, not just a source dump.
- [x] `HANDOFF.md` records completed work, commands/searches, gaps, and next loops.

## Forbidden Actions

- Do not invent sources or cite sources that were not inspected.
- Do not present proxy/community evidence as official product behavior.
- Do not browse authenticated/private pages unless the user explicitly asks.
- Do not keep researching after the marginal value is low; synthesize and state gaps.
- Do not modify project files unless the research task explicitly includes a file deliverable.

## Verification Commands

```bash
python scripts/render_worker_prompt.py workflows/auto-research-brief
python scripts/check_handoff.py workflows/auto-research-brief
```

## Current Status

- Status: workflow drafted and locally validated
- Last updated: 2026-05-09
- Current owner/session: GitHub Pattern Translator
