"""
transform.py -- TRANSFORM step
 
Shob business rule EKHANE: ki "malformed" (skip korbo), ki "duplicate"
(ekbar-i rakhbo), missing category-r default ki hobe, date-r kon kon
format accept kora hobe. Extract-e ei shob chilo na, Load-eo na --
ekhane-i thaka uchit, karon future-e rule change korte hole EKTA jaigay
dekhleই hobe.
 
Return: (cleaned_rows, stats) -- stats dict-e koyta skip hoyeche ar KENO,
shei breakdown thake (pipeline logging-r jonno).
"""

from datetime import datetime

VALID_TYPE = {"income", "expenses"}
# Raw data-te date kokhono 'YYYY-MM-DD', kokhono 'DD/MM/YYYY' -- dutoi
# real-world-e hoy (jemon: ekta bank statement vs. ekta manual entry).
DATE_FORMATS = ["%Y-%m-%d", "%d/%m/%Y"]



def _parse_date(raw_date):
    """Kichu common format try kore dekhe, mile gele ISO ('YYYY-MM-DD') e convert kore."""
    raw_date = (raw_date or "").strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(raw_date, fmt).date().isoformat()
        except ValueError:
            pass
    return None  ## kono format-i mile nai -- malformed


def _parse_amount(raw_amount):
    """'500' -> 500.0 thik ache. '', 'N/A', 'abc' -> None (malformed)."""
    raw_amount = (raw_amount or "").strip()
    if not raw_amount:
        return None
    try:
        return float(raw_amount)
    except ValueError:
        return None
 
 
def transform_transactions(raw_rows):
    cleaned = []
    seen_in_batch = set()
 
    stats = {
        "input_rows": len(raw_rows),
        "skipped_malformed": 0,
        "skipped_duplicate_in_batch": 0,
        "output_rows": 0,
    }
 
    for row in raw_rows:
        amount = _parse_amount(row.get("amount"))
        date = _parse_date(row.get("date"))
        txn_type = (row.get("type") or "").strip().lower()
 
        # Malformed = amount na, date na, ba type 'income'/'expense' er
        # baire kisu -- ei row business-e kono mane rakhena, tai skip.
        if amount is None or date is None or txn_type not in VALID_TYPE:
            stats["skipped_malformed"] += 1
            continue
 
        account = (row.get("account") or "Main Account").strip()
        category = (row.get("category") or "Uncategorized").strip() or "Uncategorized"
        description = (row.get("description") or "").strip()
 
        # In-batch duplicate: SHOMO file-r moddhei same transaction duibar
        # thakle (jemon CSV export-e accidentally 2 bar likha hoye geche).
        # Ei ta database-level duplicate check na -- shei ta load.py-r kaj
        # (already_loaded), karon oita DB-r shathe check kore, ei ta shudhu
        # EKTA batch-r vitore.
        key = (date, amount, account, description)
        if key in seen_in_batch:
            stats["skipped_duplicate_in_batch"] += 1
            continue
        seen_in_batch.add(key)
 
        cleaned.append({
            "date": date,
            "type": txn_type,
            "amount": amount,
            "account": account,
            "category": category,
            "description": description,
        })
 
    stats["output_rows"] = len(cleaned)
    return cleaned, stats
 
 
if __name__ == "__main__":
    from extract import extract_transactions
 
    raw = extract_transactions()
    cleaned, stats = transform_transactions(raw)
    print(stats)
    for row in cleaned:
        print(" ", row) 