# Week 1 Recap — Python → pandas → SQL → Database → Git

## What I built (Day 1–6, as one system)

```
Day 1 -> Python Basics           (foundations: variables, functions, loops, files)
Day 2 -> Transaction Processor   (raw logic: parsing, validating, categorizing)
Day 3 -> pandas Analyzer         (data analysis: filtering, grouping, cleaning)
Day 4 -> SQL Analytics           (querying: same insight, different tool)
Day 5 -> Database Schema         (structure: normalized, relational)
Day 6 -> Git Workflow            (process: version control, collaboration-ready)
```

These weren't 6 separate exercises — they're 6 layers of one pipeline. Raw
CSV goes in at the top; a version-controlled, normalized, queryable system
comes out at the bottom.

## Cross-check: does everything actually agree?

**pandas report (Day 3) vs SQL report (Day 4):** MATCH. Both reports, run
against the exact same 8-row sample (1 missing amount, 1 duplicate),
produce identical numbers:

```
Total Income: 5000
Total Expense: 2350
Balance: 2650
Bills: 1200 (51.1%)
Food: 850 (36.2%)
Transport: 300 (12.8%)
Top Expense: Bills - Internet + electricity (1200)
Monthly Trend: 2026-09: -2350
Missing amounts: 1 row
Duplicate rows: 1 row
```

**Flat data (Day 3/4) vs normalized schema (Day 5):** NO DATA LOST. All 8
raw rows (missing amount and duplicate included) migrated into the new
`accounts`/`categories`/`transactions`/`loans`/`investments` schema, and
`verify_report.py` confirmed the same totals come out through `JOIN`s
against the normalized tables.

## What broke (patterns across the week)

- Missing data showed up as a real problem three separate times — once in
  pandas (`fillna`/`dropna`), once in SQL (`IS NULL` instead of `= NULL`),
  and once in schema design (had to make `amount` nullable, deviating from
  the original `NOT NULL` spec, or the migration would have silently
  dropped a row).
- `[✏️ add your own repeated bug pattern here — did the same off-by-one,
  wrong data type, or forgotten edge case show up more than once?]`

## What I understood well enough to explain without notes

- Why `.groupby()` (pandas) and `GROUP BY` (SQL) do the same "split → apply
  → combine" thing, just with different syntax.
- Why normalization reduces redundancy — a category name lives in one row
  instead of being repeated on every transaction that uses it.
- Why a foreign key matters — it's what stops a transaction from pointing
  at an account or category that doesn't exist.
- `[✏️ add 1–2 more of your own]`

## What I still don't fully understand (see gap-list.md for the honest, actionable version)

`[✏️ short pointer — the real list with actions lives in gap-list.md]`
