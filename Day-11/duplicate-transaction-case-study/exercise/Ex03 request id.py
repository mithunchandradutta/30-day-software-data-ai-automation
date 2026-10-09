# Exercise 03 - Explicit request_id (idempotency key)
import uuid
from helpers import setup_database
from process_event import process_event

conn = setup_database()

# Client EKBAR request_id banay. Retry hole SHEI ekoi ID abar pathay.
request_id = str(uuid.uuid4())      # uuid4 = ekta lomba random unique text
event = {"request_id": request_id, "date": "2026-09-10", "amount": -150, "description": "Lunch"}

print("1st attempt  :", process_event(conn, event))
print("Retry (same) :", process_event(conn, event))      # network timeout-er por retry

print("\n--- 2ta ashole alada coffee (alada request_id) ---")
coffee1 = {"request_id": "req_coffee_1", "date": "2026-09-11", "amount": -80, "description": "Coffee"}
coffee2 = {"request_id": "req_coffee_2", "date": "2026-09-11", "amount": -80, "description": "Coffee"}
print("coffee #1:", process_event(conn, coffee1))
print("coffee #2:", process_event(conn, coffee2), "<- ekhon thik! duitoi save holo")

total = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
print("\nTotal transactions:", total, "(lunch 1 + coffee 2 = 3 howar kotha)")