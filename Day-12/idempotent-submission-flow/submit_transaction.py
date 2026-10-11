# submit_transaction.py - idempotency.py-r function gulo jure ekta pura flow
from idempotency import get_saved_result, claim_request, save_result


def insert_transaction(conn, event):
    """Asol business kaj: transactions table-e ekta row dhukano."""
    if event["amount"] > 0:
        tx_type = "income"
    else:
        tx_type = "expense"
    cursor = conn.execute(
        "INSERT INTO transactions (date, type, amount, description) VALUES (?, ?, ?, ?)",
        (event["date"], tx_type, event["amount"], event.get("description", "")),
    )
    return cursor.lastrowid


def submit_transaction(conn, request_id, event):
    if request_id is None or request_id == "":
        return {"status": "rejected", "reason": "request_id is required"}

    # 1) Age-i hoye gele ager result-i dao (notun kore process na)
    saved = get_saved_result(conn, request_id)
    if saved is not None:
        return {"status": "duplicate_skipped", "result": saved}

    # 2) Claim kori. Hocche na mane onno keu age claim korechhe
    if not claim_request(conn, request_id):
        return {"status": "duplicate_skipped", "result": None}

    # 3) Kaj kori. Kichu bhul hole sob bhule jai (rollback), jate pore retry kora jay
    try:
        transaction_id = insert_transaction(conn, event)
        save_result(conn, request_id, str(transaction_id))
        conn.commit()
    except Exception as error:
        conn.rollback()
        return {"status": "error", "reason": str(error)}

    return {"status": "processed", "result": str(transaction_id)}
