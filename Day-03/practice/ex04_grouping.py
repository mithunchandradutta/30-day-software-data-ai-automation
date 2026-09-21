"""
Exercise 04 -- Grouping & Aggregation  (Learn 2.5)

Run (project root theke):  python practice/ex04_grouping.py

NOTE: ekhane data ekhono DIRTY (missing + duplicate ache).
Tai number gulo ekhono ful. Ex05 e clean korar por milie dekho.
"""

import pandas as pd

df = pd.read_csv("data/transactions.csv")

# groupby = split -> apply -> combine
#   split:   category onujayi row bhag kori
#   apply:   proti group e sum() chalai
#   combine: result ekta table e joro kori

# ---------- Total by category ----------
print("=== total by category ===")
print(df.groupby("category")["amount"].sum())

# ---------- Total by type ----------
print("=== total by type ===")
print(df.groupby("type")["amount"].sum())

# ---------- Average expense per category ----------
expenses = df[df["type"] == "expense"]
print("=== average expense per category ===")
print(expenses.groupby("category")["amount"].mean())

# ---------- Transaction count per category ----------
print("=== count (NaN gonena) ===")
print(df.groupby("category")["amount"].count())
print("=== size (NaN soho sob row gone) ===")
print(df.groupby("category").size())

# ---------- agg() -- ekshathe onek function ----------
print("=== agg ===")
print(expenses.groupby("category")["amount"].agg(["sum", "mean", "count"]))

# ---------- Named aggregation ----------
summary = expenses.groupby("category").agg(
    total=("amount", "sum"),
    count=("amount", "count"),
)
print(summary)

# ---------- Multiple column groupby ----------
print(df.groupby(["type", "category"]).agg(
    total=("amount", "sum"),
    count=("amount", "count"),
))

# Ask what the number means:
# Dirty data te Food = 1050 (500 + 150 + 200 + 200), count = 4, kintu size = 5.
# Clean korar por Food = 850. Duplicate Snacks 200 duibar dhora hoyeche,
# ar missing amount row ta sum e nai, kintu size e ache.
# Mane: clean na kore number bishash kora jabe na.