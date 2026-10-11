"""
Exercise 05 -- Missing Data & Duplicates  (Learn 2.6 + 2.7)

Run (project root theke):  python practice/ex05_missing_duplicates.py
"""

import pandas as pd

# ---------- Manually kichu missing + duplicate dhukai ----------
data = {
    "date":        ["2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04", "2026-09-04", "2026-09-05"],
    "type":        ["expense", "expense", "expense", "expense", "expense", "expense"],
    "amount":      [500, None, 300, 200, 200, 150],          # 1ta amount missing
    "category":    ["Food", "Food", "Transport", "Food", "Food", "Food"],
    "description": ["Lunch", "Missing amount", None, "Snacks", "Snacks", "Groceries"],   # 1ta description missing
}
df = pd.DataFrame(data)
print("=== original ===")
print(df)

# ================== MISSING DATA ==================
print("=== isnull (True = missing) ===")
print(df.isnull())
print("=== column wise missing count ===")
print(df.isnull().sum())
print("=== missing amount row ===")
print(df[df["amount"].isnull()])

# Kno missing data calculation bhange?
# NaN + 5 = NaN, tai onekgulo operation ulta-palta result dey.
# sum() NaN skip kore, kintu mean/count e ashol sonkha bodle jay.

# ---------- fillna ----------
df["description"] = df["description"].fillna("No description")
print("=== description fillna ===")
print(df)

# Ekhane amount e fillna(0) korle ki hobe? (sudhu dekhar jonno copy te)
fake = df["amount"].fillna(0)
print("fillna(0) er por mean:", fake.mean(), "| asol mean:", df["amount"].mean())
# 0 boshale average nichhe namle jay -- fake number banano hoy!

# ---------- dropna ----------
df_clean = df.dropna(subset=["amount"])
print("=== dropna(subset=['amount']) ===")
print(df_clean)

# Question: amount missing hole delete, naki default value?
# -> DELETE (ba flag). Amount ondaj kora jay na; 0 ba average boshale fake number hoy.
# -> Description faka hole default text thik ache, karon hisabe kono prabhab pore na.

# ================== DUPLICATES ==================
cols = ["date", "amount", "category"]      # duplicate-er fingerprint

print("=== duplicated (2nd copy = True) ===")
print(df_clean.duplicated(subset=cols))

print("=== duplicate rows ===")
print(df_clean[df_clean.duplicated(subset=cols)])

print("=== duplicated(keep=False): dutoi copy dekhao ===")
print(df_clean[df_clean.duplicated(subset=cols, keep=False)])

df_final = df_clean.drop_duplicates(subset=cols)      # keep="first" default
print("=== drop_duplicates ===")
print(df_final)
print("rows:", len(df), "->", len(df_clean), "->", len(df_final))

# Real life note: same din, same amount, same category, duita alada kena-kata
# thakte pare (jemon 2ta 20 taka-r chai). Fingerprint e description ba time
# add korle false-duplicate kome.