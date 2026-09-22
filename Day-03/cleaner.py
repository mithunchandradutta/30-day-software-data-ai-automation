"""
cleaner.py --Load + Inspect + Clean 
This file is used to load and clean the data.
This is not for analysis (total, groupby, trends, etc.)

"""

import pandas as pd

REQUIRED_COLUMNS = ["date", "type", "amount", "category"]
DUPLICATE_COLUMNS = ["date", "type", "amount", "category"]
VALID_TYPES = ["income", "expense"]


def load_data(path):
    """Load data from a csv file and return a pandas DataFrame."""
    if str(path).lower().endswith(".json"):
        df = pd.read_json(path)
    else:
        df = pd.read_csv(path)

    missing_columns = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    if "description" not in df.columns:
        df["description"] = None

    return df


def inspect_data(df):
    """Inspect the data and print basic information."""
    print("Shape:", df.shape)         # (row, column)
    print("Columns:", list(df.columns))
    print()
    df.info()                         # info () nijei print kore
    print()
    print(df.describe())              # count dekle missing buza jai


def clean_data(df):
    """
    Data clean kore ar ekta report dey.
    Return: (cleaned_df, report_dict)
 
    Decision (Day 3):
      - amount missing/invalid  -> row DELETE (amount ondaj kora jay na)
      - category/description faka -> default value
      - duplicate -> ekta rakho, baki muche fel
    """
    df = df.copy()
    report = {"rows_loaded":len(df)}

    # 1) type: extra space / boro-hater lekha thik kori
    df ["type"] = df["type"].astype(str).str.strip().str.lower()
    bad_type = ~df["type"].isin(VALID_TYPES)
    report["invalid_types"] = int(bad_type.sum())
    df = df[~bad_type].copy()

    # 2) amount: text hole (jemon "abc") NaN kore dei, tarpor delete
    amount_number = pd.to_numeric(df["amount"], errors="coerce")
    report["missing_amounts"] = int(df["amount"].isnull().sum())
    report["invalid_amounts"] = int(
        (amount_number.isnull() & df["amount"].notnull()).sum()
    )
    df["amount"] = amount_number
    df = df.dropna(subset=["amount"]).copy()

    # 3) date: string theke datetime; bhul date hole NaT -> delete
    data_parsed = pd.to_datetime(df["date"], errors="coerce")
    report["invalid_dates"] = int(data_parsed.isnull().sum())
    df["date"] = data_parsed
    df = df.dropna(subset=["date"]).copy()

    # 4) faka text: delete na kore default value
    df["category"] = df["category"].fillna("Uncategorized")
    df["description"] = df["description"].fillna("No description")

    # 5) duplicate: ekta rakho baki muche felo
    is_duplicate = df.duplicated(subset=DUPLICATE_COLUMNS)
    report["duplicate_rows"] = int(is_duplicate.sum())
    df = df[~is_duplicate]
    
    report["rows_after_cleaning"] =len(df)
    return df.reset_index(drop=True), report