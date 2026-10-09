# Exercise 05 - Pura flow: valid / duplicate / malformed
from helpers import setup_database
from process_event import process_event

conn = setup_database()

good = {"request_id": "req_demo_001", "date": "2026-09-10", "amount": -150, "description": "Lunch"}
print("1) Valid event     :", process_event(conn, good))
print("2) Same event abar :", process_event(conn, good))

no_id = {"date": "2026-09-10", "amount": -150, "description": "Lunch"}          # request_id nai
bad_amount = {"request_id": "req_002", "date": "2026-09-10", "amount": "abc"}   # amount number na
print("3) request_id nai  :", process_event(conn, no_id))
print("4) amount bhul     :", process_event(conn, bad_amount))

total = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
print("\nTotal transactions:", total, "(shudhu 1 ta howar kotha)")