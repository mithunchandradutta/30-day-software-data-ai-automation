"""
transactions.py
Transaction validation + calculation logic.
"""

VALID_TYPPES = {"income", "expense"}


def is_valid_transaction(tx):
    """
    Ekটা transaction valid কিনা check kore.
    Valid howar condition:
      - dict hote hobe
      - 'type' key thakte hobe, ar shetar value 'income' ba 'expense'
      - 'amount' key thakte hobe, ar shetা number (int/float) hote hobe, negative na
      - 'category' key thakte hobe, ar shetা non-empty string hote hobe
    """
    if not isinstance(tx, dict):
        return False

    tx_type = tx.get("type")
    amount = tx.get("amount")
    category = tx.get("category")

    if tx_type not in VALID_TYPPES:
        return False

    if not isinstance(amount,(int, float)) or isinstance (amount, bool):
        return False
    if amount < 0:
        return False
    
    if not isinstance (category, str) or not category.strip():
        return False

    return True


def split_transactions(transaction):
    """
    Shob transaction ke valid ar invalid e vag kore.
    Return kore: (valid_list, invalid_list)
    """
    valid = []
    invalid = []
    for tx in transaction:
        if is_valid_transaction(tx):
            valid.append(tx)
        else:
            invalid.append(tx)
            return valid, invalid

def split_transactions(transactions):
    """
    Shob transaction ke valid ar invalid e vag kore.
    Return kore: (valid_list, invalid_list)
    """
    valid = []
    invalid = []
    for tx in transactions:
        if is_valid_transaction(tx):
            valid.append(tx)
        else:
            invalid.append(tx)
    return valid, invalid

def calculate_total_income(transactions):
    """ Shob valid income transaction er total amount calculate kore."""
    return sum(tx["amount"] for tx in transactions if tx["type"] =="income")

        
def calculate_total_expense(transactions):
     """Shob 'expense' type transaction er amount jog kore total expense felay."""
     return sum(tx["amount"] for tx in transactions if tx["type"] == "expense") 

def calculate_category_totals(transactions):
    """
    Expense transaction gulo ke category wise group kore total ber kore.
    Return kore ekta dict: {category: total_amount}
    """
    category_totals = {}
    for tx in transactions:
        if tx["type"] == "expense":
            category = tx["category"]
            category_totals[category] = category_totals.get(category, 0) + tx["amount"]
    return category_totals


def calculate_balance(total_income, total_expense):
    """Balance = Total Income - Total Expense"""
    return total_income - total_expense

def get_transaction_count(transactions):
    """Total koyta valid transaction ache shetar count.""" 
    return len(transactions)
