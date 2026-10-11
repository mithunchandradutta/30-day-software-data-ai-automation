# seed_data.py - demo-r jonno sanitized (nokol) data. Ashol financial data na!
# Chalao:  python seed_data.py     -> demo.db toiri hobe
from helpers import setup_database

SAMPLE = [
    # (date, category, type, amount, description)
    ("2026-09-01", "Salary",    "income",  25000, "Monthly salary (sample)"),
    ("2026-09-03", "Food",      "expense", -1200, "Groceries"),
    ("2026-09-07", "Food",      "expense", -3000, "Restaurants"),
    ("2026-09-09", "Transport", "expense", -1500, "Ride + fuel"),
    ("2026-09-15", "Freelance", "income",   6000, "Side project (sample)"),
    ("2026-09-20", "Utilities", "expense", -2300, "Internet + electricity"),
    ("2026-09-25", "Learning",  "expense",  -900, "Course"),
    ("2026-10-02", "Food",      "expense",  -500, "Next month - September report-e ashbe na"),
]


def add_sample_data(conn):
    for row in SAMPLE:
        conn.execute(
            "INSERT INTO transactions (date, category, type, amount, description) VALUES (?, ?, ?, ?, ?)",
            row,
        )
    conn.commit()


if __name__ == "__main__":
    conn = setup_database("demo.db")
    add_sample_data(conn)
    print("demo.db toiri hoyeche,", len(SAMPLE), "ta sample transaction shoho")
