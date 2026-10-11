# helpers.py - setup + PASSED/FAILED print (eta bujhar dorkar nai)
import os
import sqlite3


def setup_database(db_file=":memory:"):
    if db_file != ":memory:" and os.path.exists(db_file):
        os.remove(db_file)
    conn = sqlite3.connect(db_file)
    for sql_file in ["schema/transactions.sql", "schema/processed_events.sql"]:
        f = open(sql_file, "r", encoding="utf-8")
        conn.executescript(f.read())
        f.close()
    return conn


results = []


def check(name, condition):
    results.append(condition)
    if condition:
        print("PASSED  " + name)
    else:
        print("FAILED  " + name)


def summary():
    if all(results):
        print("\n=> ALL PASSED")
    else:
        print("\n=> KICHU FAILED - upore FAILED line gulo dekho")
