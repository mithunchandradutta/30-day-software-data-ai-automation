# process_event.py - Day 11-er MAIN solution
#
# Flow:
#   Event ashlo -> Validate -> Age-i process hoyeche? -> request_id "claim" -> transaction save
#
# 3 ta layer-e protection:
#   Layer 1 (client)   : client prottek request-e ekta unique request_id pathay (retry-te SAME id)
#   Layer 2 (code)     : "age-i hoyeche?" check (niche Step 2)
#   Layer 3 (database) : request_id PRIMARY KEY (niche Step 3) <- asol guarantee eta
import sqlite3


def validate(event):
    """Bhul thakle error-er message dey. Sob thik thakle None dey."""
    if "request_id" not in event or event["request_id"] == "":
        return "request_id is required"
    if "amount" not in event:
        return "amount is required"
    try:
        amount = float(event["amount"])
    except (ValueError, TypeError):      # amount "abc" ba None hole ei duita error ashe
        return "amount must be a number"
    if amount == 0:
        return "amount cannot be zero"
    if "date" not in event or len(str(event["date"])) != 10:
        return "date is required (YYYY-MM-DD)"
    return None


def process_event(conn, event):
    # Step 1: Validate
    error = validate(event)
    if error is not None:
        return {"status": "rejected", "reason": error}

    request_id = event["request_id"]

    # Step 2: Age-i process hoyeche kina dekhi
    row = conn.execute(
        "SELECT transaction_id FROM processed_events WHERE request_id = ?",
        (request_id,),
    ).fetchone()
    if row is not None:
        return {"status": "duplicate_skipped", "transaction_id": row[0]}

    # Step 3: request_id ta "claim" kori (processed_events-e likhe rakhi)
    try:
        conn.execute(
            "INSERT INTO processed_events (request_id, received_at, status) "
            "VALUES (?, datetime('now'), 'processing')",
            (request_id,),
        )
    except sqlite3.IntegrityError:
        # PRIMARY KEY bole dilo: ei request_id onno keu age-i claim kore felechhe.
        # Duita request ekshathe ashle ekhane-i duplicate-ta atke jay (race condition protection).
        row = conn.execute(
            "SELECT transaction_id FROM processed_events WHERE request_id = ?",
            (request_id,),
        ).fetchone()
        if row is None:
            return {"status": "duplicate_skipped", "transaction_id": None}
        return {"status": "duplicate_skipped", "transaction_id": row[0]}

    # Step 4: Asol transaction save kori
    amount = float(event["amount"])
    if amount > 0:
        tx_type = "income"
    else:
        tx_type = "expense"

    cursor = conn.execute(
        "INSERT INTO transactions (date, type, amount, description) VALUES (?, ?, ?, ?)",
        (event["date"], tx_type, amount, event.get("description", "")),
        # event.get("description", "") = description thakle ta, na thakle khali string
    )
    transaction_id = cursor.lastrowid    # ekhon-i insert hoya row-er id

    # Step 5: processed_events-e transaction_id likhe status 'processed' kori
    conn.execute(
        "UPDATE processed_events SET transaction_id = ?, status = 'processed' WHERE request_id = ?",
        (transaction_id, request_id),
    )

    conn.commit()   # commit na korle kichui pakka save hoy na
    return {"status": "processed", "transaction_id": transaction_id}