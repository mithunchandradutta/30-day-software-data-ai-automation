# Exercise 01 - Idempotent vs Non-idempotent (Finance Tracker operations)

Prosno: "ei kaj 5 bar korle final result ki 1 bar-er moto-i thake?"

| # | Operation | Idempotent? | Keno |
|---|---|---|---|
| 1 | `balance = balance + 500` | NO | Prottek bar balance bare |
| 2 | `balance = 1500` (set) | YES | Koto bar korlew 1500 |
| 3 | transactions-e INSERT (request_id chhara) | NO | Prottek bar notun row |
| 4 | `submit_transaction(request_id=X)` (Day 12) | YES | 2nd bar ager result dey, notun row na |
| 5 | `DELETE FROM transactions WHERE id = 7` | YES | 1st bar delete, 2nd bar-e kichu nai - state ekoi |
| 6 | Report dekha (SELECT) | YES | Kichu bodlay na |
| 7 | Report email pathano | NO (default) | Prottek bar notun email -> Day 13-e fix kora hobe |

Thumb rule: "X set koro" = idempotent. "X-e Y jog koro / notun banao" = non-idempotent.
