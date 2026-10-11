"""
verify_report.py -- Day 4-r final report notun normalized schema-r upor
abar chalie dekhay je result SAME ashe (shudhu ekhon JOIN lagbe, karon
category ekhon ekta ID, plain text na).

Ei file confirm kore: "Re-run Day 4's key queries against the new schema
and confirm results match" (Day 5 Build checklist-er last item).

Run (project root theke):
    python build_schema.py
    python verify_report.py
"""

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "finance.db"

# Day 4-r run_report.py theke pawa expected number gulo (SAME data)
EXPECTED = {
    "total_income": 5000.0,
    "total_expense": 2350.0,
    "balance": 2650.0,
    "missing_amounts": 1,
    "duplicate_rows": 1,
}


def fmt(number):
    return f"{number:.2f}".rstrip("0").rstrip(".")


def main():
    conn = sqlite3.connect(DB_PATH)

    # Notun schema-te "clean" data ber korte ekhon transactions JOIN categories
    # lagbe, karon category ekhon shudhu ekta id -- naam dorkar hole join.
    totals = conn.execute("""
        WITH valid AS (
            SELECT * FROM transactions WHERE amount IS NOT NULL
        ),
        deduped AS (
            SELECT * FROM valid
            WHERE id IN (
                SELECT MIN(id) FROM valid GROUP BY date, amount, category_id
            )
        )
        SELECT
            SUM(CASE WHEN type='income'  THEN amount ELSE 0 END),
            SUM(CASE WHEN type='expense' THEN amount ELSE 0 END),
            SUM(CASE WHEN type='income'  THEN amount ELSE -amount END)
        FROM deduped
    """).fetchone()

    breakdown = conn.execute("""
        WITH valid AS (
            SELECT * FROM transactions WHERE amount IS NOT NULL
        ),
        deduped AS (
            SELECT * FROM valid
            WHERE id IN (
                SELECT MIN(id) FROM valid GROUP BY date, amount, category_id
            )
        )
        SELECT c.name, SUM(d.amount) AS total,
               ROUND(SUM(d.amount) * 100.0 / (
                   SELECT SUM(amount) FROM deduped WHERE type = 'expense'
               ), 1) AS percent
        FROM deduped d
        JOIN categories c ON d.category_id = c.id
        WHERE d.type = 'expense'
        GROUP BY c.name
        ORDER BY total DESC
    """).fetchall()

    missing = conn.execute(
        "SELECT COUNT(*) FROM transactions WHERE amount IS NULL"
    ).fetchone()[0]

    duplicate_rows = conn.execute("""
        SELECT COALESCE(SUM(times_seen - 1), 0) FROM (
            SELECT COUNT(*) AS times_seen FROM transactions
            WHERE amount IS NOT NULL
            GROUP BY date, amount, category_id
            HAVING COUNT(*) > 1
        )
    """).fetchone()[0]

    conn.close()

    income, expense, balance = totals

    print("=== Notun schema (JOIN diye) vs Day 4 report ===")
    print(f"Total Income:  {fmt(income)}  (expected {fmt(EXPECTED['total_income'])})")
    print(f"Total Expense: {fmt(expense)}  (expected {fmt(EXPECTED['total_expense'])})")
    print(f"Balance:       {fmt(balance)}  (expected {fmt(EXPECTED['balance'])})")
    print(f"Missing amounts: {missing}  (expected {EXPECTED['missing_amounts']})")
    print(f"Duplicate rows:  {duplicate_rows}  (expected {EXPECTED['duplicate_rows']})")
    print()
    print("Category Breakdown:")
    for name, total, percent in breakdown:
        print(f"  {name}: {fmt(total)} ({percent:.1f}%)")
    print()

    checks = [
        income == EXPECTED["total_income"],
        expense == EXPECTED["total_expense"],
        balance == EXPECTED["balance"],
        missing == EXPECTED["missing_amounts"],
        duplicate_rows == EXPECTED["duplicate_rows"],
    ]
    if all(checks):
        print("MATCH: notun normalized schema Day 4-r report-er shathe hubohu mile.")
    else:
        print("MISMATCH: kono ekta number Day 4-r report-er shathe mele nai!")


if __name__ == "__main__":
    main()
