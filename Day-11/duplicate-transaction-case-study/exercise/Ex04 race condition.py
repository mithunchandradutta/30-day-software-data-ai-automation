# Exercise 04 - Race condition
#
# Race condition mane: duita request PRAY EKSHATHE ashe. Dujon-i check kore dekhe "nai",
# tarpor dujon-i insert kore.
#
# Amra thread/complex kichu use korchi na. Shudhu 2ta connection (A ar B) niye
# step gulo HATE KORE sajiye dekhachhi, ba hubohu ei order-e ghote:
#
#   1. A check kore  -> "nai"
#   2. B check kore  -> "nai"   (A ekhono insert kore ni!)
#   3. A insert kore
#   4. B insert kore            <- duplicate!
import sqlite3
from helpers import setup_database

setup_database("race_demo.db").close()     # file database (duita connection lagbe, tai file)
conn_a = sqlite3.connect("race_demo.db")
conn_b = sqlite3.connect("race_demo.db")

# ================= PART 1: database constraint CHHARA =================
print("=== PART 1: constraint chhara (check then insert) ===")
conn_a.execute("CREATE TABLE naive_events (request_id TEXT)")    # PRIMARY KEY NAI
conn_a.commit()
rid = "req_race_1"

a_saw = conn_a.execute("SELECT 1 FROM naive_events WHERE request_id = ?", (rid,)).fetchone()
b_saw = conn_b.execute("SELECT 1 FROM naive_events WHERE request_id = ?", (rid,)).fetchone()
print("A check:", a_saw, "| B check:", b_saw, "  (duitoi None = 'nai')")

if a_saw is None:
    conn_a.execute("INSERT INTO naive_events VALUES (?)", (rid,))
    conn_a.execute("INSERT INTO transactions (date, type, amount, description) VALUES ('2026-09-10','expense',-100,'race test 1')")
    conn_a.commit()
    print("A insert kore fello")
if b_saw is None:
    conn_b.execute("INSERT INTO naive_events VALUES (?)", (rid,))
    conn_b.execute("INSERT INTO transactions (date, type, amount, description) VALUES ('2026-09-10','expense',-100,'race test 1')")
    conn_b.commit()
    print("B-o insert kore fello")

count = conn_a.execute("SELECT COUNT(*) FROM transactions WHERE description = 'race test 1'").fetchone()[0]
print("Transaction row:", count, "<- BUG! 2 ta holo\n")

# ================= PART 2: PRIMARY KEY shoho =================
print("=== PART 2: processed_events.request_id PRIMARY KEY shoho ===")
rid = "req_race_2"

a_saw = conn_a.execute("SELECT 1 FROM processed_events WHERE request_id = ?", (rid,)).fetchone()
b_saw = conn_b.execute("SELECT 1 FROM processed_events WHERE request_id = ?", (rid,)).fetchone()
print("A check:", a_saw, "| B check:", b_saw, "  (ekhaneo duitoi 'nai' dekhlo)")

# A age claim kore
conn_a.execute("INSERT INTO processed_events (request_id, received_at, status) VALUES (?, datetime('now'), 'processed')", (rid,))
conn_a.execute("INSERT INTO transactions (date, type, amount, description) VALUES ('2026-09-10','expense',-100,'race test 2')")
conn_a.commit()
print("A claim + insert korlo")

# B claim korte jay - kintu database BADHA dey
try:
    conn_b.execute("INSERT INTO processed_events (request_id, received_at, status) VALUES (?, datetime('now'), 'processed')", (rid,))
    conn_b.execute("INSERT INTO transactions (date, type, amount, description) VALUES ('2026-09-10','expense',-100,'race test 2')")
    conn_b.commit()
    print("B-o insert korlo (eta hoyar kotha na!)")
except sqlite3.IntegrityError:
    conn_b.rollback()
    print("B-ke DATABASE atkalo (IntegrityError) -> B kichu save korlo na")

count = conn_a.execute("SELECT COUNT(*) FROM transactions WHERE description = 'race test 2'").fetchone()[0]
print("Transaction row:", count, "<- THIK! shudhu 1 ta")
print("\nShikha: 'check then insert' jothesto noy. PRIMARY KEY-i sesh guarantee.")

conn_a.close()
conn_b.close()