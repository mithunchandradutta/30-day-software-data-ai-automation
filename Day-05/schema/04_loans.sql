-- 04_loans.sql  (Learn 2.6)
-- Kaoke taka dhar deoya ba kaar theke dhar neoya -- ekta account-r shathe linked.

CREATE TABLE loans (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id    INTEGER NOT NULL,
    principal     REAL NOT NULL,       -- mul taka-r poriman
    interest_rate REAL,                -- % (thakte o pare, nao thakte pare)
    start_date    TEXT NOT NULL,
    due_date      TEXT,
    status        TEXT DEFAULT 'active',   -- 'active' | 'paid' | 'defaulted'
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);
