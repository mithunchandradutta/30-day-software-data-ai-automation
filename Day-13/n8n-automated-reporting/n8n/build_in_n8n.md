# n8n-e automated report banano (step by step)

Workflow:  **Schedule Trigger -> Code -> IF -> (Email / Telegram / jekono delivery node)**

1. Notun workflow kholo.
2. **Schedule Trigger** add koro:
   - Test-er jonno: Trigger Interval = `Minutes`, Every `2` minutes
   - Pore (shesh-e): `Months`, Day of Month = `1`, Hour = `8`
3. **Code** node add koro -> `n8n/report_code_node.js` er shob code paste koro.
   (Test-er shomoy `period = '2026-09';` line-ta uncomment koro.)
4. **IF** node add koro:
   - Value 1: `{{ $json.status }}`   |  Operation: `is equal to`  |  Value 2: `ready`
5. IF-er **true** branch-e delivery node:
   - **Send Email** node (SMTP credential lagbe) ba **Telegram** node, message = `{{ $json.report }}`
   - Kichu na pele ekta **Edit Fields (Set)** node diye report-ta dekhe nao.
6. IF-er **false** branch-e **No Operation** node (ei period age-i pathano hoyeche).
7. Error alert: workflow settings (upor-dane 3 dot -> Settings) -> **Error Workflow**-e ekta alada workflow
   set korte paro, ba prottek delivery node-e Settings -> `On Error` -> `Continue (using error output)` diye
   error branch-e alert node boshao.
8. Workflow **Active** koro. 2 minute por 1st run: `ready` + report. 2nd run: `skipped`
   (static data shudhu active workflow-er schedule run-e save hoy, manual "Execute" e na).
9. Recording-er por Schedule-ta abar monthly-te phirao.

## Shimaboddhota (honest)
- Code node-e data hard-coded. Ashol data-r jonno Code-er age n8n-er database node (SQLite/Postgres/Google Sheets)
  boshao ebong tar output theke `rows` banao.
- Python version (`run_report.py`) ar n8n version duita-i ekoi idea - ekta tomar computer-e, ekta n8n-e.
- Static data = learning-er jonno. Shokto guarantee-r jonno `report_log`-er moto database table lage.
