"""
test_cases.py  --  Day 3 Testing table-er 6ta test case

Run (project root theke):
    python test_cases.py
"""

from pathlib import Path

import pandas as pd

from cleaner import load_data, clean_data
from analyzer import analyze

SAMPLE_FILE = Path(__file__).resolve().parent / "data" / "transactions.csv"
COLUMNS = ["date", "type", "amount", "category", "description"]


def make_df(rows):
    return pd.DataFrame(rows, columns=COLUMNS)


def test_01_normal_load():
    """CSV thik moto load hoy: 8 row, 5 column."""
    df = load_data(SAMPLE_FILE)
    assert df.shape == (8, 5)


def test_02_missing_values():
    """Amount missing row crash kore na, delete hoy ar report e ashe."""
    df = make_df([
        ["2026-09-01", "expense", 100, "Food", "Lunch"],
        ["2026-09-02", "expense", None, "Food", "Missing amount"],
    ])
    cleaned, report = clean_data(df)
    assert report["missing_amounts"] == 1
    assert len(cleaned) == 1


def test_03_duplicate_rows():
    """Duplicate row detect hoy ar ekta thake."""
    df = make_df([
        ["2026-09-10", "expense", 200, "Food", "Snacks"],
        ["2026-09-10", "expense", 200, "Food", "Snacks"],
    ])
    cleaned, report = clean_data(df)
    assert report["duplicate_rows"] == 1
    assert len(cleaned) == 1


def test_04_empty_category():
    """Category None hole 'Uncategorized' hoy, groupby break kore na."""
    df = make_df([["2026-09-01", "expense", 100, None, "Mystery"]])
    cleaned, _ = clean_data(df)
    result = analyze(cleaned)
    assert "Uncategorized" in result["breakdown"].index


def test_05_single_row_dataset():
    """Ekta transaction hole-o valid summary ashe (expense ar income duita case)."""
    expense_only = make_df([["2026-09-01", "expense", 100, "Food", "Lunch"]])
    cleaned, _ = clean_data(expense_only)
    result = analyze(cleaned)
    assert result["totals"]["expense"] == 100
    assert result["breakdown"].loc["Food", "percent"] == 100.0

    income_only = make_df([["2026-09-01", "income", 5000, "Salary", "Pay"]])
    cleaned, _ = clean_data(income_only)
    result = analyze(cleaned)
    assert result["totals"]["balance"] == 5000
    assert result["top_expenses"] is None          # expense nai, kintu crash nai


def test_06_wrong_data_type():
    """Amount e 'abc' hole NaN hoye delete hoy ar invalid_amounts e ashe."""
    df = make_df([
        ["2026-09-01", "expense", 100, "Food", "Lunch"],
        ["2026-09-02", "expense", "abc", "Food", "Bad amount"],
    ])
    cleaned, report = clean_data(df)
    assert report["invalid_amounts"] == 1
    assert report["missing_amounts"] == 0
    assert len(cleaned) == 1


def run_all():
    tests = [(name, fn) for name, fn in globals().items() if name.startswith("test_")]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"PASSED  {name}")
        except AssertionError as error:
            failed += 1
            print(f"FAILED  {name}  {error!r}")
        except Exception as error:                     # onno kono crash
            failed += 1
            print(f"ERROR   {name}  {type(error).__name__}: {error}")
    print(f"\n{len(tests) - failed}/{len(tests)} tests passed")
    return failed


if __name__ == "__main__":
    raise SystemExit(run_all())