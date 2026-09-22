"""
test_schema.py -- Day 5 Testing table-er 6ta test case.

Proti test nijer ekta temporary in-memory SQLite database banay (schema/*.sql
diye), tarpor specific scenario check kore. Real finance.db chhoy na.

Run (project root theke):
    python test_schema.py
"""

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_DIR = BASE_DIR / "schema"
SCHEMA_FILES = [
    "01_accounts.sql", "02_categories.sql", "03_transactions.sql",
    "04_loans.sql", "05_investments.sql", "06_indexes.sql",
]


def fresh_db():
    """Notun, khali in-memory database -- shob 5 table + index soho, FK ON."""
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON;")
    for filename in SCHEMA_FILES:
        conn.executescript((SCHEMA_DIR / filename).read_text())
    return conn


def test_01_table_creation():
    """Shob 5ta table kono error chhara toiri hoy."""
    conn = fresh_db()
    tables = {
        r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        )
    }
    assert tables == {"accounts", "categories", "transactions", "loans", "investments"}


def test_02_foreign_key_violation():
    """Vul account_id diye transaction insert korle reject hoy."""
    conn = fresh_db()
    try:
        conn.execute(
            "INSERT INTO transactions (account_id, category_id, date, type, amount) "
            "VALUES (999, NULL, '2026-09-01', 'expense', 100)"
        )
        conn.commit()
        assert False, "Foreign key violation dhora porar kotha chilo, hoyni"
    except sqlite3.IntegrityError:
        pass                                    # eta-i expected

    # Valid account_id diye insert korle SUCCESS hobe
    conn.execute("INSERT INTO accounts (name, type) VALUES ('Cash', 'cash')")
    account_id = conn.execute("SELECT id FROM accounts WHERE name='Cash'").fetchone()[0]
    conn.execute(
        "INSERT INTO transactions (account_id, category_id, date, type, amount) "
        "VALUES (?, NULL, '2026-09-01', 'expense', 100)", (account_id,)
    )
    conn.commit()
    count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
    assert count == 1


def test_03_cascade_behavior():
    """
    Account delete korle transaction-er ki hoy -- ei schema-te DECISION:
    RESTRICT (block). Delete-er age transaction gulo shorate hobe, na hole
    accidentally pura history hariye jete pare.
    SQLite-e explicit ON DELETE na dile default-i RESTRICT-er moto behave kore
    (FK ON thakle child row thakte parent delete hoy na).
    """
    conn = fresh_db()
    conn.execute("INSERT INTO accounts (name, type) VALUES ('Cash', 'cash')")
    account_id = conn.execute("SELECT id FROM accounts WHERE name='Cash'").fetchone()[0]
    conn.execute(
        "INSERT INTO transactions (account_id, category_id, date, type, amount) "
        "VALUES (?, NULL, '2026-09-01', 'expense', 100)", (account_id,)
    )
    conn.commit()

    try:
        conn.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
        conn.commit()
        assert False, "Transaction thakte account delete howar kotha na"
    except sqlite3.IntegrityError:
        pass                                    # expected -- RESTRICT kaj korche

    count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
    assert count == 1                            # transaction-o thik moto ache


def test_04_duplicate_category():
    """Already existing category name abar insert korle UNIQUE constraint-e reject hoy."""
    conn = fresh_db()
    conn.execute("INSERT INTO categories (name, group_type) VALUES ('Food', 'Variable Cost')")
    conn.commit()
    try:
        conn.execute("INSERT INTO categories (name, group_type) VALUES ('Food', 'Variable Cost')")
        conn.commit()
        assert False, "Duplicate category reject howar kotha chilo"
    except sqlite3.IntegrityError:
        pass


def test_05_data_migration():
    """Day 4-r flat data (8 row) notun schema-te migrate korle row hariye jay na."""
    db_path = BASE_DIR / "data" / "finance.db"
    if not db_path.exists():
        raise AssertionError("finance.db paoa jay nai -- age 'python build_schema.py' chalao")
    conn = sqlite3.connect(db_path)
    count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
    conn.close()
    assert count == 8


def test_06_index_effect():
    """date column-e index thakle query plan-e SEARCH (index use) dekhabe, SCAN na."""
    conn = fresh_db()
    plan = conn.execute(
        "EXPLAIN QUERY PLAN SELECT * FROM transactions WHERE date = '2026-09-01'"
    ).fetchall()
    plan_text = " ".join(str(row) for row in plan).upper()
    assert "IDX_TRANSACTIONS_DATE" in plan_text or "USING INDEX" in plan_text, plan_text


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
