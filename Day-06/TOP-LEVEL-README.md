# 30-Day Software Engineering + Data + AI + Business Analytics

> Build-in-public journey by [Mithun Chandra Dutta](https://github.com/mithunchandradutta) —
> CSE student, Daffodil International University, Bangladesh

## Overview

30 days, one connected pipeline: raw financial transaction data, processed
and analyzed three different ways (plain Python, pandas, SQL), modeled into
a proper normalized database, and version-controlled like a real
engineering project — not 30 disconnected exercises.

```
Raw Transaction Data (CSV)
        |
Python Processing (Day 1-2)
        |
     +--+--+
     |     |
  pandas   SQL
 (Day 3)  (Day 4)
     |     |
     +--+--+
        |
Normalized Database Schema (Day 5)
        |
Version-Controlled, Documented Repository (Day 6)
```

## Progress (Day 1–7)

| Day | Topic | Repo |
| --- | --- | --- |
| 1 | Python basics — problem & requirements | `[✏️ day-01 repo link]` |
| 2 | Python Transaction Processor | `[✏️ day-02 repo link]` |
| 3 | pandas Transaction Analyzer | [`python-transaction-analyzer`](https://github.com/mithunchandradutta/python-transaction-analyzer) |
| 4 | SQL Transaction Analyzer | [`sql-transaction-analyzer`](https://github.com/mithunchandradutta/sql-transaction-analyzer) |
| 5 | Normalized Financial Database Schema | [`financial-database-schema`](https://github.com/mithunchandradutta/financial-database-schema) |
| 6 | Git + Engineering Workflow | `[✏️ this folder / repo link]` |
| 7 | Week 1 Review | [`week-1-review`](https://github.com/mithunchandradutta/week-1-review) |

## Technologies Used

- Python 3, pandas
- SQL (SQLite)
- Database design (normalization, foreign keys, indexes)
- Git & GitHub (branching, conventional commits, issue tracking)

## How to Explore This Repo

Each `day-0X-*` repo above is self-contained — clone it, read its own
README, `pip install -r requirements.txt` (if there is one), and run it.
No repo depends on another to run.

## Featured Projects

- **`sql-transaction-analyzer`** — rebuilds Day 3's pandas report entirely
  in SQL (SQLite), and the two reports produce identical numbers.
- **`financial-database-schema`** — normalizes the flat transaction table
  into 5 linked tables (accounts, categories, transactions, loans,
  investments) with foreign keys, indexes, and a real ER diagram.

## What I've Learned So Far

- The same financial insight (income, expense, category breakdown, data
  quality) can be produced three different ways — imperative Python logic,
  pandas, and declarative SQL — and they should all agree.
- Cleaning decisions (delete a missing value vs. flag it) are business
  decisions, not library decisions.
- Normalization isn't academic — it's the difference between renaming a
  category in one row vs. hunting through every transaction row.
- `[✏️ add 1–2 more things from your own gap-list / week1-recap]`

## Next Steps

`[✏️ Week 2 direction — APIs, automation, etc.]`
