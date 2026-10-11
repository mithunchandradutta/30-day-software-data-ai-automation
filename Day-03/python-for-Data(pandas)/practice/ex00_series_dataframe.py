"""
Ex 00 -- pandas setup, Series vs DataFrame  (Learn 2.1)

Install:  pip install pandas
Run (project root theke):  python practice/ex00_series_dataframe.py
"""

import pandas as pd

# ---------- 1) Series = ekta column (index soho) ----------
amounts = pd.Series([500, 300, 150, 1200], name="amount")
print(amounts)
print(type(amounts))
print("sum:", amounts.sum(), "| mean:", amounts.mean())

# ---------- 2) DataFrame from list of dicts (1ta dict = 1ta row) ----------
transactions = [
    {"date": "2026-09-02", "type": "expense", "amount": 500, "category": "Food"},
    {"date": "2026-09-03", "type": "expense", "amount": 300, "category": "Transport"},
    {"date": "2026-09-07", "type": "expense", "amount": 1200, "category": "Bills"},
]
df = pd.DataFrame(transactions)
print(df.head())
print(df.dtypes)

# ---------- 3) DataFrame from dict of lists (1ta key = 1ta column) ----------
data = {
    "category": ["Food", "Transport", "Bills"],
    "amount": [500, 300, 1200],
}
df2 = pd.DataFrame(data)
print(df2)

# ---------- 4) Series vs DataFrame ----------
print(type(df["amount"]))      # Series    (ekta [])
print(type(df[["amount"]]))    # DataFrame (double [[]])

# ---------- 5) CSV theke ----------
df3 = pd.read_csv("data/transactions.csv")
print(df3.head())

# Important Question: DataFrame ki dictionary of lists, naki spreadsheet?
# -> Dekhte spreadsheet-er moto, kintu vitore column-wise kaj kore:
#    proti column-er nijer dtype ache (amount = float, category = text),
#    ar ekta operation pura column e ekshathe chole (loop lagena).
#    Spreadsheet e formula cell by cell; DataFrame e operation column by column.