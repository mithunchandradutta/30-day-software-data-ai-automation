"""
build_schema.py -- schema/*.sql theke notun finance.db banay,
migration/*.sql diye Day 4-r data migrate kore, tarpor summary print kore.

Flow:
Identify entities -> Primary keys -> Foreign keys -> Normalize -> Indexes
-> Create tables -> Migrate Day 4 data -> Validate integrity -> Summary

Run (project root theke):
    python build_schema.py
"""

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "finance.db"
SCHEMA_DIR = BASE_DIR / "schema"
MIGRATION_DIR = BASE_DIR / "migration"

SCHEMA_FILES = [
    "01_accounts.sql",
    "02_categories.sql",
    "03_transactions.sql",
    "04_loans.sql",
    "05_investments.sql",
    "06_indexes.sql",
]
TABLE_FILES = SCHEMA_FILES[:5]          # indexes table na, shudhu 5 table
INDEX_FILE = SCHEMA_FILES[5]

MIGRATION_FILES = [
    "seed_accounts_categories.sql",
    "migrate_day4_data.sql",
]

DAY4_ROW_COUNT = 8       # data/day4_transactions.csv -- expected migrated rows


def build_database():
    if DB_PATH.exists():
        DB_PATH.unlink()               # fresh shuru

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")   # SQLite-e default OFF -- chalu na korle FK check-i hobe na

    # ---------- Create tables + indexes ----------
    for filename in SCHEMA_FILES:
        sql = (SCHEMA_DIR / filename).read_text()
        conn.executescript(sql)

    # ---------- Migrate Day 4 data ----------
    for filename in MIGRATION_FILES:
        sql = (MIGRATION_DIR / filename).read_text()
        conn.executescript(sql)

    conn.commit()
    return conn


def count_tables(conn):
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    return [r[0] for r in rows]


def count_indexes(conn):
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='index' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    return [r[0] for r in rows]


def print_summary(conn):
    tables = count_tables(conn)
    indexes = count_indexes(conn)
    migrated = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]

    print("========================")
    print("DATABASE SCHEMA SUMMARY")
    print("========================")
    print()
    print(f"Tables Created: {len(tables)}")
    for t in tables:
        print(f"  - {t}")
    print()
    print("Relationships:")
    print("  transactions.account_id  -> accounts.id")
    print("  transactions.category_id -> categories.id")
    print("  loans.account_id         -> accounts.id")
    print("  investments.account_id   -> accounts.id")
    print()
    print(f"Indexes Created: {len(indexes)}")
    for i in indexes:
        print(f"  - {i}")
    print()
    print("Migration Check:")
    print(f"  Day 4 flat table rows: {DAY4_ROW_COUNT}")
    print(f"  Migrated rows:         {migrated}")
    status = "PASSED" if migrated == DAY4_ROW_COUNT else "FAILED"
    print(f"  Data integrity: {status}")


if __name__ == "__main__":
    conn = build_database()
    print_summary(conn)
    conn.close()
