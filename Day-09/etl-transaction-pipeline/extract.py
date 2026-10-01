"""
extract.py -- EXTRACT step

Shudhu raw data read kore, kono cleaning/validation/business-logic NAI.
Ekhane jodi kono bug thake, bug ta "extract-er shomoy data harano" type-r
hobe -- "cleaning-r shomoy bhul decision" type-r na. Transform-er kaj
Transform-e, ekhane na.
"""

import csv
from pathlib import Path

# Script-r nijer folder-er shapekkhe default path -- CWD (tumi kon folder
# theke 'python run_pipeline.py' chalachho) ja-i hok na kyno, eta shothik
# jaigay-i khuje pabe.
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_RAW_PATH = BASE_DIR / "data" / "raw_transactions.csv"


def extract_transactions(path=None):
    """
    CSV theke raw row gula dictionary hisebe return kore -- hubohu je obostay
    file-e ache, shei obostay. Kono type conversion, kono skip, kisu na.
    """
    path = Path(path) if path else DEFAULT_RAW_PATH
    if not path.exists():
        raise FileNotFoundError(f"Raw data file paoa jay nai: {path}")

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    return rows


if __name__ == "__main__":
    rows = extract_transactions()
    print(f"Extracted: {len(rows)} raw rows")
    for row in rows[:3]:
        print(" ", row)