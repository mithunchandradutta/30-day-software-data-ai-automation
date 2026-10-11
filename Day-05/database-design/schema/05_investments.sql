-- 05_investments.sql  (Learn 2.6)
-- Kono investment (stock, DPS, mutual fund...) -- ekta account-r shathe linked.

CREATE TABLE investments (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id       INTEGER NOT NULL,
    name             TEXT NOT NULL,
    invested_amount  REAL NOT NULL,
    current_value    REAL,             -- change hote pare, tai alada column
    start_date       TEXT NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);
