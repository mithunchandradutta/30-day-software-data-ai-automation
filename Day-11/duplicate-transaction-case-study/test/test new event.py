# Run (project-er main folder theke): python tests/test_new_event.py
import sys
sys.path.append(".")      # main folder-er file gulo (helpers, process_event) import korar jonno

from helpers import setup_database, check, summary
from process_event import process_event

conn = setup_database()
event = {"request_id": "req_a1b2c3", "date": "2026-09-01", "amount": -100, "description": "Lunch"}
result = process_event(conn, event)

check("new event: status 'processed'", result["status"] == "processed")
check("new event: transaction_id ache", result["transaction_id"] is not None)

count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
check("new event: 1 ta transaction save hoyeche", count == 1)

# amount positive hole income, negative hole expense
process_event(conn, {"request_id": "r_income", "date": "2026-09-01", "amount": 5000})
types = conn.execute("SELECT type FROM transactions ORDER BY id").fetchall()
check("amount sign: -100 = expense, 5000 = income", types[0][0] == "expense" and types[1][0] == "income")

summary()