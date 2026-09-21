"""
Exercise 03 -- Sorting & Ranking  (Learn 2.4)

Run (project root theke):  python practice/ex03_sorting.py
"""

import pandas as pd

df = pd.read_csv("data/transactions.csv")

# ---------- Top 5 largest transactions ----------
# Income (5000) o transaction, tai eta list e ashbe
top5 = df.sort_values("amount", ascending=False).head(5)
print("=== top 5 largest ===")
print(top5)

# ---------- Top 5 smallest transactions ----------
# NaN sort e sobar shesh e jay, tai missing row ekhane ashbe na
bottom5 = df.sort_values("amount", ascending=True).head(5)
print("=== top 5 smallest ===")
print(bottom5)

# Shortcut: nlargest / nsmallest
print(df.nlargest(3, "amount"))
print(df.nsmallest(3, "amount"))

# ---------- Sort by date ----------
# ISO format (YYYY-MM-DD) string hisebe-o thik moto sort hoy,
# kintu ex06 te amra datetime e convert korbo (beshi safe)
by_date = df.sort_values("date")
print("=== by date ===")
print(by_date)

# ---------- Multiple column sort ----------
print(df.sort_values(["category", "amount"], ascending=[True, False]))

# ---------- sort_index ----------
print(by_date.sort_index())            # original order e ferot

# ---------- rank ----------
df["amount_rank"] = df["amount"].rank(ascending=False)
print(df[["description", "amount", "amount_rank"]])