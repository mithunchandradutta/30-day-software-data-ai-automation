"""
setup_db.py -- CSV theke SQLite database (finance.db) banay

Ei script "queries/01_load_and_inspect.sql"-er "Load CSV into SQL Database"
step ta Python diye kore dey (sqlite3-r CSV import command-line thekeo
kora jay, kintu script rakhle re-run kora shohoj ar cross-platform).

Run (project root theke):
    python setup_db.py
"""

import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "finance.db"
CSV_PATH = BASE_DIR / "data" / "transactions.csv"
SCHEMA_PATH = BASE_DIR / "queries" / "00_schema.sql"
SEED_PATH = BASE_DIR / "queries" / "00_seed.sql"


def build_database():
    if DB_PATH.exists():
        DB_PATH.unlink()             # fresh শুরু -- prottekবার notun database

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA_PATH.read_text())      # table toiri
    conn.executescript(SEED_PATH.read_text())         # categories bhorai

    # CSV theke transactions table-e row insert
    # (khali amount = NULL, jate SQL-e IS NULL diye dhora jay)
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            amount = row["amount"].strip()
            rows.append((
                row["date"],
                row["type"],
                float(amount) if amount else None,
                row["category"],
                row["description"],
            ))

    conn.executemany(
        "INSERT INTO transactions (date, type, amount, category, description) "
        "VALUES (?, ?, ?, ?, ?)",
        rows,
    )
    conn.commit()

    count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
    print(f"finance.db toiri hoyeche -- {count} row loaded (raw, uncleaned).")
    conn.close()


if __name__ == "__main__":
    build_database()