# idempotency.py - Day 11-er logic-ke CHHOTO CHHOTO reusable function-e bhag kora
#
# Day 11-e shob ekta function-e chhilo. Ekhon 3 ta alada kaj-e bhag korlam, jate
# je kono kaj-er (transaction, report, ...) shathe jora jay:
#
#   get_saved_result()  -> ei request_id age-i hoyeche? hoye thakle result dao
#   claim_request()     -> request_id "claim" koro (PRIMARY KEY-r upor nirbhor kore)
#   save_result()       -> kaj shesh hole result likhe rakho
import sqlite3


def get_saved_result(conn, request_id):
    """Age-i hoye thakle ager result (text) dey. Na hole None."""
    row = conn.execute(
        "SELECT result FROM processed_events WHERE request_id = ? AND status = 'processed'",
        (request_id,),
    ).fetchone()
    if row is None:
        return None
    return row[0]


def claim_request(conn, request_id):
    """True = claim korte perechhi (ami-i prothom). False = onno keu age-i claim korechhe."""
    try:
        conn.execute(
            "INSERT INTO processed_events (request_id, received_at, status) "
            "VALUES (?, datetime('now'), 'processing')",
            (request_id,),
        )
        return True
    except sqlite3.IntegrityError:
        return False


def save_result(conn, request_id, result):
    conn.execute(
        "UPDATE processed_events SET result = ?, status = 'processed' WHERE request_id = ?",
        (result, request_id),
    )
