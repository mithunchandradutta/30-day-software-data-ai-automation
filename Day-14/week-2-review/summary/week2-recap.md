# Week 2 Recap (Day 8-13)

| Day | Project | Ki banalam | Core lesson |
|---|---|---|---|
| 8 | `api-transaction-fetcher` | Currency rate fetcher: GET, status check, JSON parse, field validation, error handling | `200` mane data thik na - external data shob shomoy validate koro |
| 9 | `etl-transaction-pipeline` | Extract/Transform/Load: raw CSV -> normalized schema, re-run safe | "Ekbar chole" jothesto na - 2nd bar nirapode chalano-i asol test |
| 10 | `n8n-first-workflow` | Webhook -> Validate -> Transform -> HTTP Request -> Respond | n8n no-code na: glue node diye, complex logic Code node-e |
| 11 | `duplicate-transaction-case-study` | Real Finance Tracker bug -> request_id + DB PRIMARY KEY protection | Guarantee database layer-e thake, button disable-e na |
| 12 | `idempotent-submission-flow` | Reusable idempotency library + HTTP API + idempotent n8n workflow | Reliability ekta fix na - principle, prottek layer-e |
| 13 | `n8n-automated-reporting` | Schedule -> query -> report -> deliver, idempotent + error alert | Silent failure automation na thaka-r cheyeo bipjjonok |

## Ek line-e
**API -> ETL -> n8n -> Duplicate Protection -> Idempotency -> Automated Reporting**

## Jei thread ta shob jorlo: Idempotency
- Day 11: ekta specific bug-er fix (`request_id` + PRIMARY KEY)
- Day 12: reusable principle (`check_or_process`, n8n-te-o)
- Day 13: ekdom alada context-e (report period = idempotency key)
Same idea, 3 jayga.
