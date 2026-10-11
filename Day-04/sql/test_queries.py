"""
test_queries.py -- Day 4 Testing table-er 6ta test case, SQL query-r upor.

Proti test nijer ekta temporary in-memory SQLite database banay (queries/00_schema.sql
diye), test-er jonno kichu row insert kore, tarpor query chalie result check kore.
Ei jonno test_cases.py (Day 3) real finance.db chhoy na -- alada, safe database.

Run (project root theke):
    python test_queries.py
"""

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_SQL = (BASE_DIR / "queries" / "00_schema.sql").read_text()
SEED_SQL = (BASE_DIR / "queries" / "00_seed.sql").read_text()


def fresh_db():
    """Notun, khali in-memory database -- proti test aparokrom."""
    conn = sqlite3.connect(":memory:")
    conn.executescript(SCHEMA_SQL)
    return conn


def insert(conn, rows):
    conn.executemany(
        "INSERT INTO transactions (date, type, amount, category, description) "
        "VALUES (?, ?, ?, ?, ?)",
        rows,
    )
    conn.commit()


def test_01_normal_load():
    """CSV theke loaded transactions.csv thik 8 row, 5+1(id) column."""
    conn = sqlite3.connect(BASE_DIR / "data" / "finance.db")
    count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
    columns = [c[1] for c in conn.execute("PRAGMA table_info(transactions)")]
    conn.close()
    assert count == 8, f"row count {count}"
    assert set(columns) == {"id", "date", "type", "amount", "category", "description"}


def test_02_missing_values():
    """Ekta row-e amount NULL -- query crash kore na, IS NULL diye dhora jay."""
    conn = fresh_db()
    insert(conn, [
        ("2026-09-01", "expense", 100, "Food", "Lunch"),
        ("2026-09-02", "expense", None, "Food", "Missing amount"),
    ])
    missing = conn.execute(
        "SELECT COUNT(*) FROM transactions WHERE amount IS NULL"
    ).fetchone()[0]
    assert missing == 1


def test_03_duplicate_rows():
    """Duita hubohu shomo row -- GROUP BY + HAVING COUNT(*) > 1 diye dhora jay."""
    conn = fresh_db()
    insert(conn, [
        ("2026-09-10", "expense", 200, "Food", "Snacks"),
        ("2026-09-10", "expense", 200, "Food", "Snacks"),
    ])
    dup_groups = conn.execute("""
        SELECT COUNT(*) FROM (
            SELECT date, amount, category FROM transactions
            GROUP BY date, amount, category HAVING COUNT(*) > 1
        )
    """).fetchone()[0]
    assert dup_groups == 1


def test_04_empty_category():
    """Category NULL hole groupby crash kore na, alada group hisebe dekhay."""
    conn = fresh_db()
    insert(conn, [("2026-09-01", "expense", 100, None, "Mystery")])
    result = conn.execute(
        "SELECT category, SUM(amount) FROM transactions GROUP BY category"
    ).fetchall()
    assert len(result) == 1
    assert result[0][0] is None                 # NULL nijer group


def test_05_single_row_dataset():
    """Ekta transaction hole-o valid (trivial) summary ashe."""
    conn = fresh_db()
    insert(conn, [("2026-09-01", "expense", 100, "Food", "Lunch")])
    total = conn.execute(
        "SELECT SUM(amount) FROM transactions WHERE type='expense'"
    ).fetchone()[0]
    assert total == 100

    empty_income = conn.execute(
        "SELECT SUM(amount) FROM transactions WHERE type='income'"
    ).fetchone()[0]
    assert empty_income is None                 # income nai, kintu crash nai


def test_06_join_mismatch():
    """category_id/name match na korleo INNER bad dey, LEFT NULL soho rakhe."""
    conn = fresh_db()
    conn.executescript(SEED_SQL)                 # categories table bhorai
    insert(conn, [("2026-09-15", "expense", 400, "Entertainment", "Movie")])

    inner = conn.execute("""
        SELECT COUNT(*) FROM transactions t
        INNER JOIN categories c ON t.category = c.name
        WHERE t.category = 'Entertainment'
    """).fetchone()[0]

    left = conn.execute("""
        SELECT c.group_type FROM transactions t
        LEFT JOIN categories c ON t.category = c.name
        WHERE t.category = 'Entertainment'
    """).fetchone()[0]

    assert inner == 0            # INNER JOIN: match nai, tai bad
    assert left is None          # LEFT JOIN: row thake, group_type = NULL


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