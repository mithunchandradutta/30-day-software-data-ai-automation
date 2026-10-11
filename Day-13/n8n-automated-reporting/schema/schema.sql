CREATE TABLE transactions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,       -- YYYY-MM-DD
    category    TEXT NOT NULL,
    type        TEXT NOT NULL,       -- 'income' ba 'expense'
    amount      REAL NOT NULL,
    description TEXT
);

-- Ekta period (jemon '2026-09') er report 1 bar-i gele ekhane likha hoy.
-- period PRIMARY KEY = Day 11/12-er request_id-r moto kaj kore.
CREATE TABLE report_log (
    period  TEXT PRIMARY KEY,
    sent_at TEXT NOT NULL
);
