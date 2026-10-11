# check_all_days.py - Day 11, 12, 13 er test ekshathe chalay.
#
# Shorto: 4 ta repo folder EKOI parent folder-e thakte hobe:
#   parent/
#     duplicate-transaction-case-study/
#     idempotent-submission-flow/
#     n8n-automated-reporting/
#     week-2-review/          <- ei file ekhane
#
# Chalao (week-2-review folder-er bhitore giye):  python check_all_days.py
import os
import sys

here = os.getcwd()                  # ekhon je folder-e achi (week-2-review)
parent = os.path.dirname(here)      # tar upor-er folder

tests = [
    ("duplicate-transaction-case-study", "tests/test_new_event.py"),
    ("duplicate-transaction-case-study", "tests/test_duplicate_event.py"),
    ("duplicate-transaction-case-study", "tests/test_race_condition.py"),
    ("idempotent-submission-flow", "tests/test_idempotency.py"),
    ("n8n-automated-reporting", "tests/test_report.py"),
]

for folder, test_file in tests:
    path = os.path.join(parent, folder)
    if not os.path.exists(path):
        print("MISSING folder:", path)
        continue
    print("\n##### " + folder + " / " + test_file)
    os.chdir(path)                                       # oi folder-e jai
    os.system('"' + sys.executable + '" ' + test_file)   # test chalai

os.chdir(here)
print("\nSob test-er output-e 'ALL PASSED' ache kina dekho. 'FAILED' thakle oi project-e giye dekho.")
