# n8n Automated Reporting (Day 13/30)

Database theke data ane -> report banay -> pathay. **Idempotent** (same mash-er report 2 bar jay na) ar
**error hole alert dey** (chupchap fail kore na).

## Kivabe chalabe (Python 3.9+, kono install lagbe na)
```
python seed_data.py          # demo.db toiri + sample data (nokol, ashol na)
python run_report.py         # 1st bar: sent
python run_report.py         # 2nd bar: skipped (duplicate jay ni!)
python tests/test_report.py
```
Mash bodlate `run_report.py`-r `PERIOD = "2026-09"` line-ta bodlao.
n8n part: `n8n/build_in_n8n.md`.

## Poro-r order
| # | File | Ki shikhbe |
|---|---|---|
| 1 | `schema/schema.sql` | `report_log` table - `period PRIMARY KEY` = Day 11-er request_id-r moto |
| 2 | `queries/monthly_summary.sql` | Category-wise SUM/COUNT query |
| 3 | `report_logic.py` | **Main code**: data ana -> report banano -> pathano -> mark -> alert |
| 4 | `run_report.py` | Oi function gulo chalay |
| 5 | `tests/test_report.py` | Proof (empty period, duplicate, query fail) |
| 6 | `n8n/` | Schedule trigger-shoho n8n workflow |
| 7 | `sample-output/sample_report.txt` | Report dekhte kemon |

## Idempotent delivery (Day 12-er principle, notun jaygay)
```
already_sent(period)?  --yes-->  skip (duplicate report jabe na)
        | no
   data ano -> report banao -> pathao -> mark_sent(period)
```
Pathate bhul hole `mark_sent` hoy na, tai pore abar chalale retry hoy.

## Error alert
`run_report()` pura kaj `try ... except` er bhitore. Kono step-e bhul hole `ALERTS.log`-e likhe + print kore.
**Keno?** Report chupchap na ashle tumi bhabo shob thik ache - eta no-automation-er cheye bipjjonok.

## Notun je jinis gulo
| Jinis | Mane |
|---|---|
| `strftime('%Y-%m', date) = ?` | date theke "2026-09" ongsho ber kore milay |
| `SUM(ABS(amount))`, `COUNT(*)`, `GROUP BY` | jog, gonona, group kore (Day 5-er SQL) |
| `open(file, "w")`, `.write()`, `.close()` | file-e lekha ("a" = shesh-e jog) |
| `"\n".join(lines)` | list-er shob line newline diye jora |
| `os.makedirs(folder, exist_ok=True)` | folder na thakle banay |
| `def run_report(conn, period, out_folder="outputs")` | default value: na dile "outputs" dhore |

## Honest limitations
- Duita run **thik ekshathe** shuru hole (manual + schedule) theoretically duita-i `already_sent` check pass korte pare;
  `report_log.period PRIMARY KEY` shesh protection (2nd `mark_sent` error dey). Fully race-proof banate Day 11-er "age claim koro" pattern lagbe.
- Report shudhu file-e save hoy. Email/Telegram n8n-e kora hoy.

## Debug log
| Bug | Cause | Solution | Learning |
|---|---|---|---|
|  |  |  |  |

## Commit message
`feat: build idempotent scheduled reporting workflow with n8n`
