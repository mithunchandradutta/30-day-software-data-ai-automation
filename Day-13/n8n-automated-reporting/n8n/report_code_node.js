// n8n "Code" node (Schedule Trigger-er pore). Language: JavaScript, Mode: Run Once for All Items
//
// Ei node 4 ta kaj kore:
//   1. Ager mash-er period ber kore (jemon '2026-09')
//   2. Static data (notebook) dekhe: ei period-er report age pathano hoyeche kina (idempotent)
//   3. Sample data theke report text banay  (ashol workflow-e ekhane database/Sheets node-er data boshbe)
//   4. Period-ke "pathano hoyeche" likhe rakhe

// ---- 1. Period ----
const now = new Date();
const prev = new Date(now.getFullYear(), now.getMonth() - 1, 1);
let period = prev.getFullYear() + '-' + String(prev.getMonth() + 1).padStart(2, '0');
// Test-er shomoy ei line-er comment tule period fixed koro:
// period = '2026-09';

// ---- 2. Idempotent check ----
const staticData = $getWorkflowStaticData('global');
if (!staticData.sentPeriods) {
  staticData.sentPeriods = {};
}
if (staticData.sentPeriods[period]) {
  return [{ json: { status: 'skipped', period: period } }];     // age-i pathano hoyeche
}

// ---- 3. Report banano (sample data) ----
const rows = [
  { category: 'Salary',    type: 'income',  total: 25000 },
  { category: 'Freelance', type: 'income',  total: 6000 },
  { category: 'Food',      type: 'expense', total: 4200 },
  { category: 'Transport', type: 'expense', total: 1500 },
];

let report = 'Monthly Report - ' + period + '\n' + '='.repeat(30) + '\n';
let income = 0;
let expense = 0;

if (rows.length === 0) {
  report += 'No transactions this period.';
} else {
  for (const row of rows) {
    report += row.type + ' | ' + row.category + ' | ' + row.total + '\n';
    if (row.type === 'income') { income += row.total; } else { expense += row.total; }
  }
  report += '-'.repeat(30) + '\n';
  report += 'Total income : ' + income + '\n';
  report += 'Total expense: ' + expense + '\n';
  report += 'Net          : ' + (income - expense);
}

// ---- 4. Mark sent ----
staticData.sentPeriods[period] = new Date().toISOString();

return [{ json: { status: 'ready', period: period, report: report } }];
