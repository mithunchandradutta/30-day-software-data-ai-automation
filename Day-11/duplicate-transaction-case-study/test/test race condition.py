# Run: python tests/test_race_condition.py
# (ex04_race_condition.py-r moto, kintu check() diye)
import sys
import sqlite3
sys.path.append(".")

from helpers import setup_database, check, summary

setup_database("race_test.db").close()
conn_a = sqlite3.connect("race_test.db")
conn_b = sqlite3.connect("race_test.db")
rid = "req_race"

# duitoi check kore "nai" dekhlo
a_saw = conn_a.execute("SELECT 1 FROM processed_events WHERE request_id = ?", (rid,)).fetchone()
b_saw = conn_b.execute("SELECT 1 FROM processed_events WHERE request_id = ?", (rid,)).fetchone()
check("duita connection-i 'nai' dekhlo", a_saw is None and b_saw is None)

# A insert kore
conn_a.execute("INSERT INTO processed_events (request_id, received_at, status) VALUES (?, datetime('now'), 'processed')", (rid,))
conn_a.execute("INSERT INTO transactions (date, type, amount, description) VALUES ('2026-09-10','expense',-100,'race')")
conn_a.commit()

# B insert korte gele database atkay
blocked = False
try:
    conn_b.execute("INSERT INTO processed_events (request_id, received_at, status) VALUES (?, datetime('now'), 'processed')", (rid,))
    conn_b.commit()
except sqlite3.IntegrityError:
    blocked = True
    conn_b.rollback()

check("2nd insert database atkalo (PRIMARY KEY)", blocked)
count = conn_a.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
check("shudhu 1 ta transaction", count == 1)

conn_a.close()
conn_b.close()
summary()