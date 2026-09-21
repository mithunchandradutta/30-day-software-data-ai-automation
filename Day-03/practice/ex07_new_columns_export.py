"""
Exercise 07 -- New Columns, Transformations & Exporting
(Learn 2.8 + 2.10)

Run from project root:
python practice/ex07_new_columns_export.py
"""

import pandas as pd


# ---------- 1. Load CSV ----------

df = pd.read_csv("data/transactions.csv")

# Normalize column names:
# Remove extra spaces and convert names to lowercase
df.columns = df.columns.str.strip().str.lower()

print("Column names:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())


# ---------- 2. Check Required Columns ----------

required_columns = ["date", "type", "amount", "category", "description"]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}. "
        f"Available columns: {df.columns.tolist()}"
    )


# ---------- 3. Clean Data ----------

# Convert amount to numeric
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Remove rows with missing amounts
df = df.dropna(subset=["amount"]).copy()

# Remove duplicate transactions
df = df.drop_duplicates(
    subset=["date", "amount", "category"]
).copy()


# ---------- 4. New Column: amount_signed ----------

# Income = positive
# Expense = negative

df["amount_signed"] = df.apply(
    lambda row: (
        row["amount"]
        if row["type"] == "income"
        else -row["amount"]
    ),
    axis=1,
)

print("\nAmount Signed:")
print(df[["type", "amount", "amount_signed"]])


# ---------- 5. Same Operation: 3 Ways ----------

# Method 1: Normal loop

signed_loop = []

for _, row in df.iterrows():
    signed_loop.append(
        row["amount"]
        if row["type"] == "income"
        else -row["amount"]
    )


# Method 2: apply()
# Already performed above in amount_signed


# Method 3: Vectorization

signed_fast = df["amount"].where(
    df["type"] == "income",
    -df["amount"],
)


# Compare results

print(
    "\nLoop and Vectorized results same?",
    signed_loop == list(signed_fast),
)

print(
    "Apply and Vectorized results same?",
    df["amount_signed"].equals(signed_fast.rename("amount_signed")),
)


# ---------- 6. Type Conversion ----------

df["amount_int"] = df["amount"].astype(int)

print("\nData Types:")
print(df.dtypes)


# ---------- 7. Create a Label Column ----------

# Combine category and description

df["label"] = (
    df["category"].astype("string")
    + " - "
    + df["description"].astype("string")
)

print("\nLabels:")
print(df[["label", "amount"]])


# ---------- 8. Expense Summary ----------

summary = (
    df[df["type"] == "expense"]
    .groupby("category")
    .agg(
        total=("amount", "sum"),
        count=("amount", "count"),
    )
)

print("\nExpense Summary:")
print(summary)


# ---------- 9. Export CSV ----------

summary.to_csv(
    "data/practice_summary.csv",
    index_label="category",
)


# ---------- 10. Export JSON ----------

summary.to_json(
    "data/practice_summary.json",
    orient="index",
    indent=2,
)


# ---------- 11. Read Exported CSV ----------

summary_check = pd.read_csv(
    "data/practice_summary.csv",
    index_col="category",
)

print("\nRead Exported CSV:")
print(summary_check)


# ---------- 12. Completion Message ----------

print("\nSaved successfully:")
print("data/practice_summary.csv")
print("data/practice_summary.json")