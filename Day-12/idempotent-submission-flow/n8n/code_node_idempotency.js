// n8n "Code" node-e boshabe (Language: JavaScript, Mode: Run Once for All Items)
//
// Ekhane Day 11-er idea-i, kintu n8n-er nijer "static data" (workflow-er bhitore ekta chhoto notebook)
// e request_id gulo mone rakha hocche.

const staticData = $getWorkflowStaticData('global');     // workflow-er notebook
if (!staticData.processed) {
  staticData.processed = {};                              // prothom bar hole khali notebook banai
}

const body = $input.first().json.body;                    // Webhook-er pathano data
const requestId = body.request_id;

// Step 1: validate
if (!requestId) {
  throw new Error('request_id is required');
}

// Step 2: age-i hoyeche?
if (staticData.processed[requestId]) {
  return [{ json: { status: 'duplicate_skipped', result: staticData.processed[requestId] } }];
}

// Step 3: notun request -> kaj kori (ekhane shudhu ekta fake transaction id banachhi)
const transactionId = 'txn_' + Date.now();
staticData.processed[requestId] = transactionId;          // notebook-e likhe rakhi

return [{ json: { status: 'processed', result: transactionId } }];
