"""
analyzer.py  --  Transform + Group + Rank + Export
 
Clean data nie analysis kore. Load/clean ekhane hobe na -- oita cleaner.py te.
"""

import pandas as pd 


def add_signed_amount(df):
    """ income = +amount, expense = -amount."""
    df = df.copy()
    if df.empty:
        df["amount_signed"] = pd.Series(dtype="float64")
        return df

    # .apply(axis=1) mane row by row python function chalano (slow, kintu bujha easy)
    df["amount_signed"] = df.apply(
        lambda row: row["amount"] if row["type"] == 'income' else -row["amount"],
        axis=1
    )
    # Faster (vectorized) version:
    # df["amount_signed"] = df["amount"].where(df["type"] == "income", -df["amount"])
    return df


def add_date_columns (df):
    """date theke month ar day_name column banai."""
    df = df.copy()
    df["date"]= pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    df["day_name"] = df["date"].dt.day_name()
    return df


def calculate_totals(df):
    total_income = df.loc[df["type"] == "income", "amount"].sum()
    total_expenses = df.loc[df["type"] == "expense", "amount"].sum()
    return{
        "income": total_income,
        "expense": total_expenses,
        "balance": total_income - total_expenses,
    }


def category_breakdown(df):
    """
    Expense-er category wise total, count, percent.
    groupby = split -> apply -> combine
    """
    expenses = df[df["type"] == "expense"]
    if expenses.empty:
        return pd.DataFrame(columns=["total", "count", "percent"])

    summary = expenses.groupby("category", sort=False).agg(
        total=("amount", "sum"),
        count=("amount", "count"),
    )
    summary["percent"] = (summary["total"] / summary["total"].sum() * 100).round(1)
    # ami jodi Ranking chai tahole ai formula use korte hobbe point to be noted: summary = summary.sort_values("total", ascending=False)
    return summary


def top_and_bottom_expenses(df):
    """Sobcheye boro ar sobcheye choto expense row. Expense na thakle (None, None)."""
    expenses = df[df["type"] == "expense"]
    if expenses.empty:
        return None, None
    top = expenses.loc[expenses["amount"].idxmax()]
    bottom = expenses.loc[expenses["amount"].idxmin()]
    return top, bottom


def monthly_trend(df):
     """Maser hisabe spending (expense negative hisebe: -2350)."""
     expenses = df[df["type"] == "expense"]
     return expenses.groupby("month") ["amount_signed"].sum()


def analyze(df):
    """Pura analysis ekshathe chalay, result dict e dey."""
    df = add_signed_amount(df)
    df = add_date_columns(df)
    top, bottom = top_and_bottom_expenses(df)
    return{
        "df": df,
        "totals": calculate_totals(df),
        "breakdown": category_breakdown(df),
        "top_expenses": top,
        "lowest_expenses": bottom,
        "monthly_trend": monthly_trend(df),
    }


def export_category_summary(breakdown, path):
    """Category summary CSV te save kore."""
    breakdown.to_csv(path)
 