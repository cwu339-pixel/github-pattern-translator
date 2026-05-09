---
name: validate-quant-research
description: Use when validating a quantitative trading strategy, factor, alpha claim, backtest, portfolio rule, or research run that needs reproducible evidence, leakage/bias checks, cost/slippage assumptions, risk metrics, and handoff before implementation or promotion.
---

# Validate Quant Research

## Overview

Turn quant ideas, notebooks, and prototype backtests into auditable research
runs. Optimize for reproducibility, leakage control, evidence quality, and clear
handoff before changing strategy logic or claiming alpha.

## Operating Rule

Start with an audit unless the user explicitly asks for implementation. Do not
place trades, touch live execution, or call a result "validated" without a
config, data window, command, and artifact trail.

If the user wants a prompt for another session, output only the execution prompt
and acceptance criteria. If the user wants execution here, inspect local files
first and keep edits scoped.

## Workflow

1. **Scope the claim**
   - Identify the strategy/factor, asset universe, timeframe, frequency, and
     target decision: explore, validate, compare, or promote.
   - Separate hypothesis, implementation, data, results, and open assumptions.

2. **Map the data flow**
   - Trace raw data -> cleaned data -> features -> signal -> position -> PnL ->
     metrics.
   - Record data source, timestamp semantics, timezone, missing-data handling,
     resampling, corporate actions, funding, and benchmark source when relevant.

3. **Check leakage and bias before reading returns**
   - Look for future data in features, labels, normalization, ranking, joins,
     calendar alignment, and order fill assumptions.
   - Check survivorship bias, selection bias, lookahead bias, same-bar execution,
     target leakage, and parameter tuning on the test set.

4. **Verify backtest assumptions**
   - Require fees, slippage, spread, funding/borrow, latency, capacity, turnover,
     position limits, leverage, and liquidation or margin rules when applicable.
   - Mark omissions as assumptions or blockers, not harmless details.

5. **Run the smallest reproducible check**
   - Prefer a focused command or notebook cell path that regenerates one result.
   - Capture command, config, git state if available, data window, and output
     paths.

6. **Build or review the evidence package**
   - Store results under a run-specific directory when possible.
   - Keep proxy evidence separate from official evidence.
   - Never overwrite prior runs unless the user explicitly asks.

## Evidence Package

Prefer this structure, adapted to the repo:

```text
research_runs/<strategy-or-factor>/<run-id>/
  strategy_spec.md
  data_audit.md
  backtest_config.yaml
  metrics.csv
  trades.csv
  equity_curve.csv
  risk_report.md
  leakage_check.md
  assumptions.md
  handoff.md
```

If the project already has a different results layout, follow it and map these
concepts into existing files.

## Minimum Acceptance Criteria

- Results map to a config, data window, and command.
- Data timing semantics are explicit.
- In-sample, out-of-sample, walk-forward, or holdout boundaries are explicit.
- Fees, slippage, and execution assumptions are stated.
- Leakage checks are documented with pass/fail/unknown.
- Risk metrics include at least return, volatility or Sharpe, max drawdown,
  turnover, hit rate or win rate, exposure, and trade count when applicable.
- Trade log or position series can explain the main source of PnL.
- Failed or rejected assumptions are recorded, not hidden.

## Output Formats

### Audit response

```text
Strategy context
Data/source audit
Signal/formula flow
Backtest assumptions
Leakage/bias risks
Evidence package status
Next execution plan
Handoff state
```

### Handoff state

```text
Current paths:
Completed:
Not completed:
Commands run:
Artifacts produced:
Current pass/fail:
Known risks:
Next open loops:
```

## Common Mistakes

- Optimizing for the prettiest equity curve before leakage checks.
- Reporting the best parameter sweep without failed runs or selection logic.
- Using full-sample normalization, ranking, or feature scaling.
- Generating a signal from a bar and filling on the same bar without an explicit
  execution assumption.
- Omitting fees, slippage, funding, borrow, spread, or turnover.
- Treating proxy data or synthetic cases as official validation.
- Letting notebooks become the only source of truth instead of exporting config
  and artifacts.
