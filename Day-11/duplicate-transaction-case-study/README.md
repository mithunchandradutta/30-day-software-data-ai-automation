# Duplicate Transaction Case Study (Day 11/30)

Amar Finance Tracker-er real duplicate-transaction bug theke shikhe banano server-side protection.

## Kivabe chalabe
Python lagbe (3.9+). Kono pip install lagbe na.
Terminal-e **ei folder-er bhitore** giye:
```
python ex01_reproduce.py        <- bug dekho
python ex02_fingerprint.py      <- purono fix + tar weakness
python ex03_request_id.py       <- notun fix
python ex04_race_condition.py   <- race condition + PRIMARY KEY
python ex05_end_to_end.py       <- pura flow
python tests/test_new_event.py
python tests/test_duplicate_event.py
python tests/test_race_condition.py
```
(Mac/Linux-e `python` na cholle `python3` likho.)

## Poro-r order
| # | File | Ki shikhbe |
|---|---|---|
| 1 | `ex01_reproduce.py` | Duplicate bug kemon hoy |
| 2 | `ex02_fingerprint.py` | Fingerprint approach, tar weakness |
| 3 | `schema/processed_events.sql` | `PRIMARY KEY` ki |
| 4 | `process_event.py` | **Main code** - 5 ta step, prottek step-e comment |
| 5 | `ex03_request_id.py` | request_id diye kaj korano |
| 6 | `ex04_race_condition.py` | Race condition step by step |
| 7 | `ex05_end_to_end.py` | Valid / duplicate / malformed |
| 8 | `tests/` | Proof ye shob thik kaj korche |
| - | `helpers.py` | Shudhu setup (database banay, PASSED/FAILED print kore) - eta bujhar dorkar nai |

## `process_event.py`-r 5 step
```
Step 1  Validate          bhul data hole rejected
Step 2  Age-i hoyeche?    processed_events-e request_id ache? thakle skip
Step 3  Claim             processed_events-e INSERT (PRIMARY KEY duplicate hole error)
Step 4  Save              transactions-e INSERT
Step 5  Update + commit   processed_events-e transaction_id likhe commit
```

## Ei project-e ja ja use hoyeche (cheat sheet)
| Jinis | Mane |
|---|---|
| `conn = sqlite3.connect("x.db")` | database-er sathe connection |
| `conn.execute("SQL", (value,))` | SQL chalao. `?` jaygay value boshe (safe way) |
| `.fetchone()` | 1 ta row anbe; na thakle `None` |
| `.fetchall()` | shob row-er list |
| `conn.commit()` | ekhon porjonto-r kaj pakka save koro |
| `conn.rollback()` | commit-er age-r kaj bhule jao |
| `PRIMARY KEY` | ei column-e ekoi value 2 bar thakte parbe na |
| `try: ... except sqlite3.IntegrityError:` | try koro; PRIMARY KEY-r moto rule bhangle `except`-er code chalao |
| `row is None` / `is not None` | kichu nai / kichu ache |
| `dict["key"]`, `dict.get("key", "")` | dictionary theke value; `.get` hole key na thakleo error dey na |
| `cursor.lastrowid` | ekhon-i insert kora row-er id |
| `import uuid; str(uuid.uuid4())` | unique random ID banay |

## Race condition ki? (shobcheye important idea)
```
A: check "ache?" -> nai          B: check "ache?" -> nai
A: INSERT                        B: INSERT      <- duplicate!
```
`ex04_race_condition.py` ei step gulo hate kore sajiye dekhay. Part 1-e duplicate hoy, Part 2-te PRIMARY KEY B-ke atkay.

## Debug log (nijer bug ekhane likho)
| Bug | Cause | Solution | Learning |
|---|---|---|---|
|  |  |  |  |

## Commit message
`fix: add server-side idempotent duplicate protection with request_id`