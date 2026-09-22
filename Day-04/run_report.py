"""
run_report.py -- queries/06_final_report.sql chalie Day 3-r moto
readable report print kore.

Ei file KONO analysis nijer hate kore na -- shudhu SQL query gulo
run kore, result-ke print-friendly banay. Ashol kaj (clean, group,
aggregate) sob SQL-e, queries/06_final_report.sql-e.

Run (project root theke):
    python setup_db.py     # 1 bar, ba data change hole
    python run_report.py
"""

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "finance.db"


def fmt(number):
    """5000.0 -> '5000', -2350.0 -> '-2350'."""
    return f"{number:.2f}".rstrip("0").rstrip(".")


def rows(count):
    return f"{count} row" if count == 1 else f"{count} rows"


def main():
    if not DB_PATH.exists():
        print("finance.db paoa jay nai. Age 'python setup_db.py' chalao.")
        return

    conn = sqlite3.connect(DB_PATH)

    totals = conn.execute("""
        WITH valid AS (SELECT * FROM transactions WHERE amount IS NOT NULL),
             deduped AS (
                 SELECT * FROM valid
                 WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
             )
        SELECT
            SUM(CASE WHEN type='income'  THEN amount ELSE 0 END),
            SUM(CASE WHEN type='expense' THEN amount ELSE 0 END),
            SUM(CASE WHEN type='income'  THEN amount ELSE -amount END)
        FROM deduped
    """).fetchone()

    breakdown = conn.execute("""
        WITH valid AS (SELECT * FROM transactions WHERE amount IS NOT NULL),
             deduped AS (
                 SELECT * FROM valid
                 WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
             ),
             expense_totals AS (
                 SELECT category, SUM(amount) AS total
                 FROM deduped WHERE type = 'expense'
                 GROUP BY category
             )
        SELECT category, total,
               ROUND(total * 100.0 / (SELECT SUM(total) FROM expense_totals), 1)
        FROM expense_totals
        ORDER BY total DESC
    """).fetchall()

    top_expense = conn.execute("""
        WITH valid AS (SELECT * FROM transactions WHERE amount IS NOT NULL),
             deduped AS (
                 SELECT * FROM valid
                 WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
             )
        SELECT category, description, amount FROM deduped
        WHERE type = 'expense' ORDER BY amount DESC LIMIT 1
    """).fetchone()

    lowest_expense = conn.execute("""
        WITH valid AS (SELECT * FROM transactions WHERE amount IS NOT NULL),
             deduped AS (
                 SELECT * FROM valid
                 WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
             )
        SELECT category, description, amount FROM deduped
        WHERE type = 'expense' ORDER BY amount ASC LIMIT 1
    """).fetchone()

    trend = conn.execute("""
        WITH valid AS (SELECT * FROM transactions WHERE amount IS NOT NULL),
             deduped AS (
                 SELECT * FROM valid
                 WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
             )
        SELECT strftime('%Y-%m', date), SUM(-amount)
        FROM deduped WHERE type = 'expense'
        GROUP BY 1
    """).fetchall()

    missing = conn.execute(
        "SELECT COUNT(*) FROM transactions WHERE amount IS NULL"
    ).fetchone()[0]

    duplicate_rows = conn.execute("""
        SELECT COALESCE(SUM(times_seen - 1), 0) FROM (
            SELECT COUNT(*) AS times_seen FROM transactions
            WHERE amount IS NOT NULL
            GROUP BY date, amount, category
            HAVING COUNT(*) > 1
        )
    """).fetchone()[0]

    conn.close()

    print("========================")
    print("SQL TRANSACTION ANALYSIS REPORT")
    print("========================")
    print()
    print(f"Total Income: {fmt(totals[0])}")
    print(f"Total Expense: {fmt(totals[1])}")
    print(f"Balance: {fmt(totals[2])}")
    print()

    print("Category Breakdown:")
    if not breakdown:
        print("(no expenses)")
    for category, total, percent in breakdown:
        print(f"{category}: {fmt(total)} ({percent:.1f}%)")
    print()

    if top_expense:
        cat, desc, amt = top_expense
        print(f"Top Expense: {cat} - {desc} ({fmt(amt)})")
    if lowest_expense:
        cat, desc, amt = lowest_expense
        print(f"Lowest Expense: {cat} - {desc} ({fmt(amt)})")
    print()

    print("Monthly Trend:")
    if not trend:
        print("(no data)")
    for month, value in trend:
        print(f"{month}: {fmt(value)}")
    print()

    print("Data Quality:")
    print(f"Missing amounts: {rows(missing)}")
    print(f"Duplicate rows: {rows(duplicate_rows)}")


if __name__ == "__main__":
    main()