# n8n-e idempotent workflow banano (step by step)

3 ta node:  **Webhook -> Code -> Respond to Webhook**

1. n8n-e notun workflow kholo.
2. **Webhook** node add koro:
   - HTTP Method: `POST`
   - Path: `idempotent-transaction`
   - Respond: `Using 'Respond to Webhook' Node`
3. **Code** node add koro (Webhook-er pore jora dao):
   - Language: JavaScript
   - `n8n/code_node_idempotency.js` file-er shob code paste koro
4. **Respond to Webhook** node add koro (Code-er pore):
   - Respond With: `First Incoming Item`
5. Workflow-ke **Active** koro (upore-dane toggle). Eta MUST - karon "static data" shudhu active workflow-er
   production run-e save hoy. "Test workflow" button-e chalale kichu mone thake na.
6. Webhook node-e **Production URL** ta copy koro (`.../webhook/idempotent-transaction`, "webhook-test" na).
7. `n8n/send_twice.py`-te URL boshao, `python n8n/send_twice.py` chalao.
8. n8n -> **Executions** tab-e duita run dekho. 1st: processed, 2nd: duplicate_skipped, same result.

## Ei n8n version-er shimaboddhota (honest)
- Eta learning version: request_id gulo n8n-er notebook-e thake, tai database-level PRIMARY KEY-r moto
  shokto guarantee na. Production-e Day 11-er moto database lagbe (n8n-er Postgres/SQLite/Sheets node diye).
- Transaction-id ta fake (`txn_` + shomoy). Asol-e ekhane database-e INSERT-er node boshbe.
