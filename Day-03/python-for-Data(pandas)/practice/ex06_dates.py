"""
Exercise 06 -- Dates  (Learn 2.9)

Run (project root theke):  python practice/ex06_dates.py
"""

import pandas as pd

df = pd.read_csv("data/transactions.csv")

# Age quick clean (full clean ache cleaner.py te)
df = df.dropna(subset=["amount"]).drop_duplicates(subset=["date", "amount", "category"])

# ---------- date column -> datetime ----------
print("age:", df["date"].dtype)
df["date"] = pd.to_datetime(df["date"])
print("pore:", df["date"].dtype)

# ---------- month, year, day, day name ----------
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.to_period("M")     # 2026-09
df["day"] = df["date"].dt.day
df["day_name"] = df["date"].dt.day_name()      # Monday, Tuesday ...
print(df[["date", "year", "month", "day", "day_name"]])

# ---------- Group total spending by month ----------
expenses = df[df["type"] == "expense"]
monthly = expenses.groupby("month")["amount"].sum()
print("=== monthly spending ===")
print(monthly)

# ---------- Day of week with highest spending ----------
by_weekday = expenses.groupby("day_name")["amount"].sum().sort_values(ascending=False)
print("=== spending by weekday ===")
print(by_weekday)
print("Highest spending day:", by_weekday.idxmax(), "->", by_weekday.max())

# ---------- Time-based filtering ----------
after_5 = df[df["date"] >= "2026-09-05"]
print("=== 2026-09-05 er por ===")
print(after_5)

between = df[df["date"].between("2026-09-02", "2026-09-07")]
print("=== 02 theke 07 ===")
print(between)

# Ask what the number means:
# Ekta weekday tey beshi spend keno? Ekta boro bill (1200) ki pura pattern-ke
# dhake dichhe? Choto data te weekday pattern-er upor beshi bhorosha kora jay na.