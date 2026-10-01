"""
test_pipeline.py -- Day 9 Testing table-er 6ta test case.

Proti test nijer temporary in-memory SQLite database ar synthetic raw rows
use kore (sample CSV-r upor depend kore na), tai test gula deterministic.

Run (project root theke):
    python test_pipeline.py
"""

import sqlite3
from pathlib import Path

from transform import transform_transactions
from load import get_or_create, transaction_already_loaded, load_transactions

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_SQL = (BASE_DIR / "schema.sql").read_text()


def fresh_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript(SCHEMA_SQL)
    return conn


def test_01_clean_extract():
    """Shudhu valid row -- shob kota row-i transform-er por bere ashe."""
    rows = [
        {"date": "2026-09-01", "type": "income", "amount": "5000", "category": "Salary",
         "description": "Pay", "account": "Main Account"},
        {"date": "2026-09-02", "type": "expense", "amount": "500", "category": "Food",
         "description": "Lunch", "account": "Main Account"},
    ]
    cleaned, stats = transform_transactions(rows)
    assert stats["output_rows"] == 2
    assert stats["skipped_malformed"] == 0


def test_02_malformed_row():
    """Missing/invalid amount-wala row skip hoy, pipeline crash kore na."""
    rows = [
        {"date": "2026-09-01", "type": "expense", "amount": "", "category": "Food",
         "description": "Missing amount", "account": "Main Account"},
        {"date": "2026-09-02", "type": "expense", "amount": "N/A", "category": "Food",
         "description": "Bad amount", "account": "Main Account"},
        {"date": "2026-09-03", "type": "expense", "amount": "100", "category": "Food",
         "description": "Valid one", "account": "Main Account"},
    ]
    cleaned, stats = transform_transactions(rows)
    assert stats["skipped_malformed"] == 2
    assert stats["output_rows"] == 1


def test_03_in_batch_duplicate():
    """Ekই file-e same transaction duibar thakle, EKTA-i load hoy."""
    rows = [
        {"date": "2026-09-10", "type": "expense", "amount": "200", "category": "Food",
         "description": "Snacks", "account": "Main Account"},
        {"date": "2026-09-10", "type": "expense", "amount": "200", "category": "Food",
         "description": "Snacks", "account": "Main Account"},
    ]
    cleaned, stats = transform_transactions(rows)
    assert stats["skipped_duplicate_in_batch"] == 1
    assert stats["output_rows"] == 1

    conn = fresh_db()
    cursor = conn.cursor()
    loaded, _ = load_transactions(cursor, cleaned)
    assert loaded == 1


def test_04_rerun_safety():
    """Shei SAME cleaned data dui bar load korle, dwitiyo bar 0 notun row."""
    rows = [
        {"date": "2026-09-01", "type": "expense", "amount": "300", "category": "Transport",
         "description": "Bus", "account": "Main Account"},
    ]
    cleaned, _ = transform_transactions(rows)

    conn = fresh_db()
    cursor = conn.cursor()

    loaded_first, skipped_first = load_transactions(cursor, cleaned)
    conn.commit()
    assert loaded_first == 1
    assert skipped_first == 0

    loaded_second, skipped_second = load_transactions(cursor, cleaned)
    conn.commit()
    assert loaded_second == 0
    assert skipped_second == 1

    total = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
    assert total == 1          # duplicate toiri hoyni


def test_05_new_category():
    """Category DB-te na thakle, get_or_create nijei notun row banay."""
    conn = fresh_db()
    cursor = conn.cursor()

    before = conn.execute("SELECT COUNT(*) FROM categories").fetchone()[0]
    category_id = get_or_create(cursor, "categories", "Freelance")
    conn.commit()
    after = conn.execute("SELECT COUNT(*) FROM categories").fetchone()[0]

    assert after == before + 1
    # Abar call korle SAME id ferot ashe, notun row toiri hoy na
    again_id = get_or_create(cursor, "categories", "Freelance")
    assert again_id == category_id
    after_again = conn.execute("SELECT COUNT(*) FROM categories").fetchone()[0]
    assert after_again == after


def test_06_foreign_key_integrity():
    """Load howar por, proti transaction-r account_id/category_id REAL row-ke point kore."""
    rows = [
        {"date": "2026-09-01", "type": "expense", "amount": "600", "category": "Shopping",
         "description": "New shoes", "account": "Cash"},
    ]
    cleaned, _ = transform_transactions(rows)

    conn = fresh_db()
    cursor = conn.cursor()
    load_transactions(cursor, cleaned)
    conn.commit()

    orphan_accounts = conn.execute(
        "SELECT COUNT(*) FROM transactions WHERE account_id NOT IN (SELECT id FROM accounts)"
    ).fetchone()[0]
    orphan_categories = conn.execute(
        "SELECT COUNT(*) FROM transactions "
        "WHERE category_id IS NOT NULL AND category_id NOT IN (SELECT id FROM categories)"
    ).fetchone()[0]

    assert orphan_accounts == 0
    assert orphan_categories == 0


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
        except Exception as error:
            failed += 1
            print(f"ERROR   {name}  {type(error).__name__}: {error}")
    print(f"\n{len(tests) - failed}/{len(tests)} tests passed")
    return failed


if __name__ == "__main__":
    raise SystemExit(run_all())