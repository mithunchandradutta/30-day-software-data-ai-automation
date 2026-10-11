# Idempotent Submission Flow (Day 12/30)

Day 11-er duplicate fix-ke **reusable function** banano + n8n-e same idea.

> Idempotency = "ekoi request 5 bar ashleo business result 1 bar-i hobe".

## Kivabe chalabe (Python 3.9+, kono install lagbe na)
```
python ex01_idempotent_or_not.py
python demo.py
python tests/test_idempotency.py
```
n8n part-er jonno `n8n/build_in_n8n.md` poro.

## Poro-r order
| # | File | Ki shikhbe |
|---|---|---|
| 1 | `ex01_idempotent_or_not.py` | Idempotent vs non-idempotent (balance example) |
| 2 | `docs/idempotency-classification.md` | Finance Tracker-er 7 ta operation classify |
| 3 | `idempotency.py` | 3 ta chhoto function: `get_saved_result`, `claim_request`, `save_result` |
| 4 | `submit_transaction.py` | Oi 3 ta function jure pura flow |
| 5 | `demo.py` | Same request_id 2 bar |
| 6 | `tests/test_idempotency.py` | Proof |
| 7 | `n8n/` | n8n-e same idea |
| 8 | `docs/idempotency-checklist.md` | Bhobishyote prottek notun kaj-e use korbe |

## Day 11 theke ki bodlalo?
Day 11-e shob ekta function-e chhilo. Ekhon **3 ta chhoto function** (check / claim / save), jate onno kaj-eo (report, order, ...) lagano jay.
Ar Day 11 shudhu `transaction_id` rakhto; ekhon **result** rakhi, jate retry-te ager-i uttor dewa jay.

## Flow (`submit_transaction`)
```
request_id nai?            -> rejected
Age-i processed?           -> ager result dao (duplicate_skipped)
Claim hocche na?           -> onno keu age-i claim korechhe (duplicate_skipped)
Kaj kori (try)             -> bhul hole rollback (retry kora jabe)
Result save + commit       -> processed
```

## Notun je jinis gulo (Day 11 theke extra)
| Jinis | Mane |
|---|---|
| `def f(conn, request_id, event):` | function-e ekadhik jinis dewa |
| `return` + `if not claim_request(...)` | function True/False dey, `not` ulte dey |
| `try ... except Exception as error:` | je kono bhul dhoro; `str(error)` e bhul-er message pabe |
| `for attempt in range(5):` | 5 bar loop |
| `from idempotency import a, b, c` | onno file theke function ana |

## Debug log
| Bug | Cause | Solution | Learning |
|---|---|---|---|
|  |  |  |  |

## Commit message
`feat: generalize duplicate-protection into a reusable idempotency library used by both code and n8n`
