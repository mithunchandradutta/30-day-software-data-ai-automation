# Exercise 01 - Problem-ta reproduce kori: kono duplicate check nai
from helpers import setup_database

conn = setup_database()


def add_transaction_no_check(conn, date, amount, description):
    conn.execute(
        "INSERT INTO transactions (date, type, amount, description) VALUES (?, 'expense', ?, ?)",
        (date, amount, description),
    )
    conn.commit()


# User "Submit" button-e double-click korlo -> ekoi data 2 bar gelo
add_transaction_no_check(conn, "2026-09-10", -150, "Lunch")
add_transaction_no_check(conn, "2026-09-10", -150, "Lunch")
 
rows = conn.execute("SELECT * FROM transactions").fetchall()
for row in rows:
    print(row)
print("\nTotal row:", len(rows), "<- BUG! 1 ta howar kotha chhilo, 2 ta hoye gelo")