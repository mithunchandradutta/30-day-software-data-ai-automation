# Run (main folder theke): python tests/test_idempotency.py
import sys
sys.path.append(".")

from helpers import setup_database, check, summary
from submit_transaction import submit_transaction

event = {"date": "2026-09-10", "amount": -150, "description": "Lunch"}

# --- new request ---
conn = setup_database()
r1 = submit_transaction(conn, "req_1", event)
check("new request: processed", r1["status"] == "processed")

# --- duplicate request ---
r2 = submit_transaction(conn, "req_1", event)
check("duplicate: duplicate_skipped", r2["status"] == "duplicate_skipped")
check("duplicate: ager-i result ferot dilo", r2["result"] == r1["result"])
count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
check("duplicate: notun row hoy ni", count == 1)

# --- alada request_id ---
r3 = submit_transaction(conn, "req_2", event)
check("alada request_id: processed", r3["status"] == "processed")

# --- request_id nai ---
check("request_id nai: rejected", submit_transaction(conn, "", event)["status"] == "rejected")

# --- fail hole retry kora jay ---
conn2 = setup_database()
bad_event = {"date": "2026-09-10", "description": "amount nai"}     # amount missing -> bhul
r_bad = submit_transaction(conn2, "req_retry", bad_event)
check("bhul event: error", r_bad["status"] == "error")
left = conn2.execute("SELECT COUNT(*) FROM processed_events").fetchone()[0]
check("bhul event: claim rollback hoyeche", left == 0)
good_event = {"date": "2026-09-10", "amount": -50, "description": "ok"}
check("retry (same request_id, thik data): processed", submit_transaction(conn2, "req_retry", good_event)["status"] == "processed")

summary()
