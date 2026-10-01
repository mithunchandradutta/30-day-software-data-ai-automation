"""
load.py -- LOAD step

Cleaned row gula ekhon schema.sql-r table-e boshate hobe. Duita kaj:
  1. account/category naam -> id resolve kora ("get or create" pattern)
  2. transaction insert kora -- kintu AGE check kora eta age-theke-i
     database-e ache kina (re-run safety / idempotent load)

Extract/Transform-e kono DB touch hoyni -- shudhu EKHANE.
"""


def get_or_create(cursor, table, name):
    """
    `table`-e `name` thakle oi id return kore, na thakle notun row banay.
    Day 5-r normalization-r practical dik -- raw data-te category/account
    shudhu ekta string, kintu schema-te oita ekta foreign-key id hote hobe.
    """
    cursor.execute(f"SELECT id FROM {table} WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row:
        return row[0]

    cursor.execute(f"INSERT INTO {table} (name) VALUES (?)", (name,))
    return cursor.lastrowid


def transaction_already_loaded(cursor, date, amount, account_id, description):
    """
    Natural key = date + amount + account_id + description. Ei row age
    theke-i transactions table-e thakle, pipeline eta abar insert korbe na --
    eta-i re-run safety: SAME pipeline SAME file-r upor dui/tin bar chalale-o
    duplicate transaction toiri hobe na.
    """
    cursor.execute("""
        SELECT 1 FROM transactions
        WHERE date = ? AND amount = ? AND account_id = ? AND description = ?
    """, (date, amount, account_id, description))
    return cursor.fetchone() is not None


def load_transactions(cursor, cleaned_rows):
    """
    Return: (loaded_count, skipped_duplicate_count)
    """
    loaded = 0
    skipped_duplicate = 0

    for row in cleaned_rows:
        account_id = get_or_create(cursor, "accounts", row["account"])
        category_id = get_or_create(cursor, "categories", row["category"])

        if transaction_already_loaded(cursor, row["date"], row["amount"], account_id, row["description"]):
            skipped_duplicate += 1
            continue

        cursor.execute("""
            INSERT INTO transactions (account_id, category_id, date, type, amount, description)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (account_id, category_id, row["date"], row["type"], row["amount"], row["description"]))
        loaded += 1

    return loaded, skipped_duplicate