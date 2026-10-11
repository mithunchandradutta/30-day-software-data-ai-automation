# Python Transaction Analyzer (pandas)

> Day 3/30 — Python for Data | 30 Days of Software Engineering + Data + AI + Business Analytics
> by [Mithun Chandra Dutta](https://github.com/mithunchandradutta)

## Overview

A small command-line tool that takes exported financial transactions (CSV/JSON), cleans them with pandas, and produces a report that answers real questions: where does the money go, what is the biggest expense, and how trustworthy is the data?

The rule for this project: **don't just run pandas functions — ask what each number actually says about the money.**

## Features

- Loads transactions from CSV or JSON
- Data inspection (`--inspect`: shape, dtypes, `info()`, `describe()`)
- Cleaning pipeline: missing amounts, invalid (text) amounts, invalid dates, invalid types, empty categories, duplicate rows
- Total income, total expense and balance
- Category-wise totals, counts and percentages
- Highest and lowest single expense
- Monthly spending trend
- Data-quality report (missing / duplicate / invalid rows)
- Exports the category summary to `data/category_summary.csv`
- 6 test cases covering the edge cases from the Day 3 testing table

## Technologies

- Python 3
- pandas

## Project Structure

```
python-transaction-analyzer/
│
├── main.py                 # runs the pipeline and prints the report
├── analyzer.py             # transform, group, rank, export
├── cleaner.py              # load, inspect, clean
├── test_cases.py           # 6 test cases (plain asserts, no extra library)
├── requirements.txt
│
├── data/
│   ├── transactions.csv        # sample data (intentional missing + duplicate rows)
│   └── category_summary.csv    # generated output
│
├── practice/               # Day 3 learning + practice lab scripts
│   ├── ex00_series_dataframe.py
│   ├── ex01_load_inspect.py
│   ├── ex02_filtering.py
│   ├── ex03_sorting.py
│   ├── ex04_grouping.py
│   ├── ex05_missing_duplicates.py
│   ├── ex06_dates.py
│   └── ex07_new_columns_export.py
│
├── README.md
└── .gitignore
```

Loading/cleaning, analysis and the entry point are kept in separate files so each part can be changed and tested without touching the others.

## How to Run

```bash
# 1. Install pandas
pip install -r requirements.txt

# 2. Run the analyzer (from the project root)
python main.py

# Optional: show info() and describe() first
python main.py --inspect

# Optional: use your own file
python main.py data/my_transactions.csv

# 3. Run the tests
python test_cases.py

# 4. Run a practice script
python practice/ex04_grouping.py
```

## Example Input

`data/transactions.csv`

```csv
date,type,amount,category,description
2026-09-01,income,5000,Salary,September salary
2026-09-02,expense,500,Food,Lunch with friends
2026-09-03,expense,300,Transport,Bus + rickshaw
2026-09-05,expense,150,Food,Groceries
2026-09-07,expense,1200,Bills,Internet + electricity
2026-09-10,expense,,Food,Missing amount
2026-09-10,expense,200,Food,Snacks
2026-09-10,expense,200,Food,Snacks
```

## Example Output

```
========================
TRANSACTION ANALYSIS REPORT
========================

Total Income: 5000
Total Expense: 2350
Balance: 2650

Category Breakdown:
Food: 850 (36.2%)
Transport: 300 (12.8%)
Bills: 1200 (51.1%)

Top Expense: Bills - Internet + electricity (1200)
Lowest Expense: Food - Groceries (150)

Monthly Trend:
2026-09: -2350

Data Quality:
Missing amounts: 1 row
Duplicate rows: 1 row
```

**What the numbers say:** Bills are 51% of all spending, but they are close to fixed costs. Food (36%) is the category where spending can realistically be reduced.

## Data Quality Handling

| Problem | Decision | Why |
| --- | --- | --- |
| Missing amount | Delete the row and report it | An amount cannot be guessed; filling with `0` or the average creates fake numbers |
| Text in amount (e.g. `"abc"`) | Convert to `NaN` (`errors="coerce"`), delete, report as invalid | Same reason as above, but counted separately |
| Invalid date | Convert to `NaT`, delete, report | Trend analysis needs a real date |
| Invalid `type` (not income/expense) | Delete and report | The sign of the amount depends on it |
| Empty category / description | Fill with `Uncategorized` / `No description` | The amount is still valid, so the row is kept |
| Duplicate rows | Keep the first, remove the rest (fingerprint = `date + amount + category`) | Same transaction counted twice inflates spending |

Without cleaning, Food would show 1050 instead of 850 — a wrong number that looks correct.

## What I Learned

**pandas**
- A `Series` is one column; a `DataFrame` is a table of Series sharing one index
- Boolean filtering, `.loc` / `.iloc`, `.query()`
- `groupby` = split → apply → combine
- `.agg()` with multiple functions, `count()` vs `size()`
- Missing data (`isnull`, `fillna`, `dropna`) and duplicates (`duplicated`, `drop_duplicates`)
- Dates with `pd.to_datetime()` and `.dt`
- `.apply()` vs a plain loop vs vectorized operations

**Software engineering**
- Separating loading, cleaning and analysis logic
- Validating data quality *before* trusting the numbers
- Handling edge cases with tests (single row, empty category, wrong data type)

**Data**
- A number is easy to get; understanding what it means is the real work
- Cleaning decisions (delete vs fill) are business decisions, not library decisions

## Future Improvements

- Flag suspected duplicates for review instead of deleting them silently
- Validate negative amounts
- Support multiple months and a month-over-month comparison
- Add charts
- Move on to SQL (Day 4) and query the same data with `GROUP BY`