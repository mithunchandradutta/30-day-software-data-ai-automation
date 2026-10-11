# Run (main folder theke): python tests/test_report.py
import os
import shutil
import sqlite3
import sys
sys.path.append(".")

from helpers import setup_database, check, summary
from seed_data import add_sample_data
from report_logic import get_summary, build_report_text, run_report

OUT = "test_outputs"
if os.path.exists(OUT):
    shutil.rmtree(OUT)          # purono test output muchi

conn = setup_database()
add_sample_data(conn)

# --- 1. Report sothik? ---
rows = get_summary(conn, "2026-09")
text = build_report_text("2026-09", rows)
check("report: total income 31000", "Total income : 31000" in text)
check("report: total expense 8900", "Total expense: 8900" in text)
check("report: net 22100", "Net          : 22100" in text)
check("report: October-er data ashe ni", "Next month" not in text)

# --- 2. Empty period ---
empty_text = build_report_text("2026-01", get_summary(conn, "2026-01"))
check("empty period: 'No transactions' bole, crash kore na", "No transactions this period" in empty_text)

# --- 3. Pathano ---
check("1st run: sent", run_report(conn, "2026-09", OUT) == "sent")
check("report file toiri hoyeche", os.path.exists(OUT + "/report_2026-09.txt"))

# --- 4. Idempotent re-run ---
check("2nd run (same period): skipped", run_report(conn, "2026-09", OUT) == "skipped")
count = conn.execute("SELECT COUNT(*) FROM report_log WHERE period = '2026-09'").fetchone()[0]
check("report_log-e 1 ta-i entry", count == 1)

# --- 5. Onno period alada ---
check("onno period (2026-10): sent", run_report(conn, "2026-10", OUT) == "sent")

# --- 6. Query fail hole alert ---
broken_conn = sqlite3.connect(":memory:")       # kono table-i nai!
check("query fail: status 'error'", run_report(broken_conn, "2026-09", OUT) == "error")
check("query fail: ALERTS.log toiri hoyeche", os.path.exists(OUT + "/ALERTS.log"))

shutil.rmtree(OUT)
summary()
