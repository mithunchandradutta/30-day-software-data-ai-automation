# run_report.py - report chalanor script
#   Prothome:   python seed_data.py
#   Tarpor:     python run_report.py            (1st bar -> sent)
#               python run_report.py            (2nd bar -> skipped, duplicate jay ni)
import sqlite3
from report_logic import run_report, build_report_text, get_summary

PERIOD = "2026-09"      # <- kon mash-er report? ekhane bodlao (format: YYYY-MM)

conn = sqlite3.connect("demo.db")
status = run_report(conn, PERIOD)

print("period =", PERIOD, "| status =", status)
if status == "sent":
    print("report save hoyeche: outputs/report_" + PERIOD + ".txt\n")
    print(build_report_text(PERIOD, get_summary(conn, PERIOD)))
elif status == "skipped":
    print("Ei period-er report age-i pathano hoyeche - duplicate pathano hoyni.")
