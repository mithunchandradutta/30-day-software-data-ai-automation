# Run: python tests/test_duplicate_event.py
import sys
sys.path.append(".")

from helpers import setup_database, check, summary
from process_event import process_event

conn = setup_database()
event = {"request_id": "req_a1b2c3", "date": "2026-09-01", "amount": -100, "description": "Lunch"}

first = process_event(conn, event)
second = process_event(conn, event)
check("duplicate: 2nd bar 'duplicate_skipped'", second["status"] == "duplicate_skipped")
check("duplicate: same transaction_id ferot dilo", second["transaction_id"] == first["transaction_id"])
count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
check("duplicate: row 1 ta-i", count == 1)

# request_id chhara
no_id = {"date": "2026-09-01", "amount": -100}
check("missing request_id: rejected", process_event(conn, no_id)["status"] == "rejected")

# bhul amount
bad = {"request_id": "req_bad", "date": "2026-09-01", "amount": "abc"}
check("malformed amount: rejected", process_event(conn, bad)["status"] == "rejected")
rows = conn.execute("SELECT COUNT(*) FROM processed_events WHERE request_id = 'req_bad'").fetchone()[0]
check("rejected event processed_events-e dhoke ni", rows == 0)

# alada request_id, same baki sob -> duitoi save hobe (fingerprint approach eta bhul korto)
c1 = {"request_id": "coffee_1", "date": "2026-09-02", "amount": -80, "description": "Coffee"}
c2 = {"request_id": "coffee_2", "date": "2026-09-02", "amount": -80, "description": "Coffee"}
r1 = process_event(conn, c1)
r2 = process_event(conn, c2)
check("alada request_id, same fields: duitoi processed", r1["status"] == "processed" and r2["status"] == "processed")

summary()