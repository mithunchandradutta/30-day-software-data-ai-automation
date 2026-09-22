"""
main.py  --  Financial Transaction Analyzer (pandas)
 
Flow:
Load -> Inspect -> Clean -> Transform -> Group/Aggregate -> Rank -> Export -> Report
 
Run:
    python main.py                       # sample data diye
    python main.py --inspect             # info() + describe() shoho
    python main.py data/my_file.csv      # nijer file diye
"""

import argparse
from pathlib import Path

from cleaner import load_data, inspect_data, clean_data
from analyzer import analyze, export_category_summary

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = BASE_DIR / "data" / "transactions.csv"
DEFAULT_OUTPUT = BASE_DIR / "data" / "category_summary.csv"


def fmt(number):
    """5000.0 -> '5000', 36.15 -> '36.15', -2350.0 -> '-2350'."""
    return f"{number:.2f}".rstrip("0").rstrip(".")
 
 
def rows(count):
    return f"{count} row" if count == 1 else f"{count} rows"
 
 
def print_report(result, quality):
    totals = result["totals"]
    breakdown = result["breakdown"]
    top = result["top_expenses"]
    lowest = result["lowest_expenses"]
    trend = result["monthly_trend"]
 
    print("========================")
    print("TRANSACTION ANALYSIS REPORT")
    print("========================")
    print()
    print(f"Total Income: {fmt(totals['income'])}")
    print(f"Total Expenses: {fmt(totals['expense'])}")
    print(f"Balance: {fmt(totals['balance'])}")
    print()
 
    print("Category Breakdown:")
    if breakdown.empty:
        print("(no expenses)")
    else:
        for category, row in breakdown.iterrows():
            print(f"{category}: {fmt(row['total'])} ({row['percent']:.1f}%)")
    print()
 
    if top is None:
        print("Top Expenses: none")
    else:
        print(f"Top Expenses: {top['category']} - {top['description']} ({fmt(top['amount'])})")
        print(f"Lowest Expenses: {lowest['category']} - {lowest['description']} ({fmt(lowest['amount'])})")
    print()
 
    print("Monthly Trend:")
    if trend.empty:
        print("(no data)")
    else:
        for month, value in trend.items():
            print(f"{month}: {fmt(value)}")
    print()
 
    print("Data Quality:")
    print(f"Missing amounts: {rows(quality['missing_amounts'])}")
    print(f"Duplicate rows: {rows(quality['duplicate_rows'])}")
    if quality["invalid_amounts"]:
        print(f"Invalid amounts (text): {rows(quality['invalid_amounts'])}")
    if quality["invalid_dates"]:
        print(f"Invalid dates: {rows(quality['invalid_dates'])}")
    if quality["invalid_types"]:
        print(f"Invalid types: {rows(quality['invalid_types'])}")
 
 
def main():
    parser = argparse.ArgumentParser(description="pandas Transaction Analyzer")
    parser.add_argument("path", nargs="?", default=str(DEFAULT_INPUT), help="CSV/JSON file")
    parser.add_argument("--inspect", action="store_true", help="info() ar describe() dekhao")
    args = parser.parse_args()
 
    try:
        df = load_data(args.path)                 # 1. Load
    except FileNotFoundError:
        print(f"File paoa jay nai: {args.path}")
        return
    except ValueError as error:
        print(f"Data problem: {error}")
        return
 
    if args.inspect:                              # 2. Inspect
        inspect_data(df)
        print()
 
    cleaned, quality = clean_data(df)             # 3. Clean
    result = analyze(cleaned)                     # 4-6. Transform, Group, Rank
    export_category_summary(result["breakdown"], DEFAULT_OUTPUT)   # 7. Export
    print_report(result, quality)                 # 8. Display
 
 
if __name__ == "__main__":
    main()