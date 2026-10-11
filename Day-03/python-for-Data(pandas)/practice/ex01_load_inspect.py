"""
Exercise 01 -- Load & Inspect  (Learn 2.2)

Run (project root theke):  python practice/ex01_load_inspect.py
"""

import io

import pandas as pd

# Load transactions.csv
df = pd.read_csv("data/transactions.csv")

# Print .head() / .tail()
print("=== head ===")
print(df.head())
print("=== tail(3) ===")
print(df.tail(3))

# .shape = (row, column)
print("shape:", df.shape)
print("columns:", list(df.columns))

# .info() -- column type + non-null count
print("=== info ===")
df.info()

# .describe() -- shudhu number column er summary
print("=== describe ===")
print(df.describe())
print(df.describe(include="all"))     # text column soho

# Column data types
print("=== dtypes ===")
print(df.dtypes)
# date, type, category, description -> text (pandas version onujayi object ba str)
# amount -> float64  (kno float? karon NaN ache; ekhane NaN thakle int hoy na)
# describe() e amount count = 7, kintu 8 row ache -> 1ta amount missing!

# ---------- JSON theke read ----------
json_text = df.head(3).to_json(orient="records")
df_json = pd.read_json(io.StringIO(json_text))
print("=== from JSON ===")
print(df_json)