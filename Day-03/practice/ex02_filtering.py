"""
Exercise 02 -- Filtering  (Learn 2.3)

Run (project root theke):  python practice/ex02_filtering.py
"""

import pandas as pd

df = pd.read_csv("data/transactions.csv")

# ---------- All expenses / All income ----------
expenses = df[df["type"] == "expense"]
income = df[df["type"] == "income"]
print("=== expenses ===")
print(expenses)
print("=== income ===")
print(income)

# ---------- Expenses above 500 ----------
# Dhyan dao: > 500 hole 500 nijei ashbe na. 500 soho chaile >= 500
above_500 = df[(df["type"] == "expense") & (df["amount"] > 500)]
print("=== expenses > 500 ===")
print(above_500)

# ---------- Specific category ----------
food = df[df["category"] == "Food"]
print("=== Food ===")
print(food)

# ---------- Multiple conditions ----------
# & = and, | = or, ar prottek condition () er vitore
food_or_bills = df[(df["category"] == "Food") | (df["category"] == "Bills")]
print("=== Food or Bills ===")
print(food_or_bills)

# isin() -- onek value check
some = df[df["category"].isin(["Food", "Transport"])]
print("=== isin ===")
print(some)

# ---------- .query() -- SQL WHERE er moto ----------
q = df.query('type == "expense" and amount > 200')
print("=== query ===")
print(q)

# ---------- .loc / .iloc ----------
print("=== loc: condition + kichu column ===")
print(df.loc[df["type"] == "expense", ["date", "category", "amount"]])
print("=== iloc: position diye (prothom 3 row, prothom 2 column) ===")
print(df.iloc[0:3, 0:2])

# ---------- Column selection ----------
print(df["amount"])                    # Series
print(df[["category", "amount"]])      # DataFrame

# Important Question: filtering vs looping?
# Filtering: 1 line, column-wise, choto ar porhte sohoj, boro data te onek druto.
# Looping:   for row in ...: if ... -- beshi line, python-level loop, dhire.