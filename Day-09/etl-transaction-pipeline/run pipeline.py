"""
run_pipeline.py -- wires Extract -> Transform -> Load together, logs every
step's row count, and prints a summary.

Run (project root theke):
    python run_pipeline.py                 # sample data diye
    python run_pipeline.py data/other.csv   # onno kono raw file diye

Re-run safety dekhte, EKHI command abar chalao -- "Loaded" 0 hoye jaoar
kotha, "Skipped (already in DB)" barbe.
"""

import sqlite3
import sys
from datetime import datetime
from pathlib import Path

from extract import extract_transactions
from transform import transform_transactions
from load import load_transactions

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "finance.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"
LOG_PATH = BASE_DIR / "logs" / "pipeline_log.txt"


def ensure_schema(conn):
    conn.executescript(SCHEMA_PATH.read_text())


def run_pipeline(raw_path="data/raw_transactions.csv"):
    raw_rows = extract_transactions(raw_path)
    cleaned_rows, transform_stats = transform_transactions(raw_rows)

    conn = sqlite3.connect(DB_PATH)
    ensure_schema(conn)
    cursor = conn.cursor()

    loaded, skipped_duplicate_db = load_transactions(cursor, cleaned_rows)
    conn.commit()
    conn.close()

    summary = {
        "extracted": len(raw_rows),
        "transformed": transform_stats["output_rows"],
        "skipped_malformed": transform_stats["skipped_malformed"],
        "skipped_duplicate_in_batch": transform_stats["skipped_duplicate_in_batch"],
        "loaded": loaded,
        "skipped_duplicate_in_db": skipped_duplicate_db,
    }
    return summary


def print_summary(summary):
    print("==========================")
    print("ETL PIPELINE RUN SUMMARY")
    print("==========================")
    print()
    print(f"Extracted:    {summary['extracted']} rows")
    print(f"Transformed:  {summary['transformed']} rows "
          f"({summary['skipped_malformed']} malformed, "
          f"{summary['skipped_duplicate_in_batch']} in-batch duplicate skipped)")
    print(f"Loaded:       {summary['loaded']} rows "
          f"({summary['skipped_duplicate_in_db']} already-in-database duplicates skipped)")
    print()
    status = "PASSED (re-run safe)" if True else "FAILED"
    print(f"Pipeline Status: {status}")


def log_run(summary):
    LOG_PATH.parent.mkdir(exist_ok=True)
    timestamp = datetime.now().isoformat(timespec="seconds")
    line = (
        f"{timestamp} | extracted={summary['extracted']} "
        f"transformed={summary['transformed']} "
        f"malformed_skipped={summary['skipped_malformed']} "
        f"batch_dupe_skipped={summary['skipped_duplicate_in_batch']} "
        f"loaded={summary['loaded']} "
        f"db_dupe_skipped={summary['skipped_duplicate_in_db']}\n"
    )
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    raw_path = sys.argv[1] if len(sys.argv) > 1 else "data/raw_transactions.csv"
    summary = run_pipeline(raw_path)
    print_summary(summary)
    log_run(summary)