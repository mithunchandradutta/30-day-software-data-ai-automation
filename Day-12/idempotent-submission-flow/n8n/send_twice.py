# Same request 2 bar n8n-e pathay. Day 8-er requests library-i lagbe (pip install requests)
import requests

# !!! Nijer n8n webhook URL boshao. "Production URL" use koro (niche README dekho)
URL = "http://localhost:5678/webhook/idempotent-transaction"

payload = {
    "request_id": "req_n8n_001",
    "date": "2026-09-10",
    "amount": -150,
    "description": "Lunch",
}

for attempt in [1, 2]:
    response = requests.post(URL, json=payload)
    print("Call", attempt, "->", response.status_code, response.text)

# Expected:
# Call 1 -> 200 {"status":"processed","result":"txn_1789..."}
# Call 2 -> 200 {"status":"duplicate_skipped","result":"txn_1789..."}   <- same result!
