"""
extract.py -- EXTRACT step
 
Shudhu raw data read kore, kono cleaning/validation/business-logic NAI.
Ekhane jodi kono bug thake, bug ta "extract-er shomoy data harano" type-r
hobe -- "cleaning-r shomoy bhul decision" type-r na. Transform-er kaj
Transform-e, ekhane na.
"""

import csv
from pathlib import Path


def extract_transactions(path="data/raw_transactions.csv"):
     """
    CSV theke raw row gula dictionary hisebe return kore -- hubohu je obostay
    file-e ache, shei obostay. Kono type conversion, kono skip, kisu na.
    """
     path = Path(path)
     if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
     
     with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

     return rows


if __name__ == "__main__":
    rows = extract_transactions()
    print(f"Extracted {len(rows)} raw rows")
    for row in rows[:3]:
        print("", row)