"""
utils.py
Helper functions: JSON load kora ar summary print kora.
"""

import json
import os


def load_transactions(filepath):
    """
    JSON file theke transaction list load kore.
    File na thakle ba invalid JSON hole empty list return kore ar error print kore.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found - {filepath}")
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
                  data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return []

    if not isinstance(data, list):
         print("Error: JSON data is not list of transactions.")
         return []
    return data



def print_summary(total_income, total_expenses, balance, category_totals,
                 transaction_count, invalid_count=0 ):
      """Formatted summary print kore, jemon expected output e deoya ache."""
      line = "=" * 24

      print(line)
      print("TRANSACTION SUMMARY")
      print(line)
      print()
      print(f"Total Income: {total_income}")
      print(f"Total Expenses : {total_expenses}")
      print(f"Balance: {balance}")
      print()
      print("Category Summary:")
      print()
      if category_totals:
           for category, total in category_totals.items():
                print(f"{category}: {total}")
           else:
                print("There is no expenses category.")
           print()
           print(f"Total Transactions: {transaction_count}")

           if invalid_count > 0:
                print(f"Invalid Transactions Skipped: {invalid_count}")

           print()
           