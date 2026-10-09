# helpers.py - chhoto kichu sahajjokari function (eta nijer kaj noy, shudhu setup)
import os
import sqlite3


def setup_database(db_file="memory:"):
    """Notun khali database banay, duita table shoho. Connection ferot dey."""
    # file hole age purono-ta muche dai, jate prottek bar fresh theke shuru hoy
    if db_file != "memory:" and os.path.exists(db_file):
        os.remove(db_file)

    conn = sqlite3.connect(db_file)

    # schema folder-er .sql file gulo pore database-e chalai
    for sql_file in ["schema/transactions.sql", "schema/processed_events.sql"]:
        f = open(sql_file, "r", encoding="utf-8")
        sql_text = f.read()
        f.close()
        conn.executescript(sql_text)  # file-er shob SQL ekshathe chalay

    return conn

# ---- test-er jonno ----
results = []