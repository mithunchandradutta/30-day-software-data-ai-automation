"""
main.py
Entry point — transaction processor run kore ekhane theke.
"""

import os

from transactions import (
    split_transactions,
    calculate_total_income,
    calculate_total_expense,
    calculate_balance,
    calculate_category_totals,
    get_transaction_count,
)
from utils import load_transactions, print_summary

# main.py file ta jei folder a ase seta base dhore path banancci.
# avabe korle ami j kono directory theke script run korleo sothik file khuje pabe. 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "transactions.json")


def main():
    raw_transactions = load_transactions(DATA_FILE)

    if not raw_transactions:
        print("No transactions found. Exiting.")
        return

    valid_transactions, invalid_transactions = split_transactions(raw_transactions)

    if invalid_transactions:
        print(f"Warning: {len(invalid_transactions)} invalid transactions found and skipped.")

    total_income = calculate_total_income(valid_transactions)
    total_expenses = calculate_total_expense(valid_transactions)
    balance = calculate_balance(total_income, total_expenses)
    category_totals = calculate_category_totals(valid_transactions)
    transaction_count = get_transaction_count(valid_transactions)

    print_summary(
        total_income,
        total_expenses,
        balance = balance,
        category_totals = category_totals,
        transaction_count=transaction_count,
        invalid_count=len(invalid_transactions)
        )


if __name__ == "__main__":
 main()