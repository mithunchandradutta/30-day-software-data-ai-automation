# demo.py - Day 12 library kaj koreche kina dekhi
from helpers import setup_database
from submit_transaction import submit_transaction

conn = setup_database()
event = {"date": "2026-09-10", "amount": -150, "description": "Lunch"}

print("call 1:", submit_transaction(conn, "req_1", event))
print("call 2:", submit_transaction(conn, "req_1", event))      # same request_id
print("call 3:", submit_transaction(conn, "req_2", event))      # notun request_id (alada kaj)
print("call 4:", submit_transaction(conn, "", event))           # request_id nai

total = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
print("\nTotal transactions:", total, "(2 ta howar kotha: req_1 + req_2)")
