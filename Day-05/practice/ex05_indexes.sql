-- Exercise 05 -- Indexes  (Practice Lab)
-- Run: sqlite3 :memory: < practice/ex05_indexes.sql

CREATE TABLE accounts (id INTEGER PRIMARY KEY, name TEXT, type TEXT);
CREATE TABLE transactions (
    id         INTEGER PRIMARY KEY,
    account_id INTEGER,
    date       TEXT,
    amount     REAL
);

-- Index chara query plan -- pura table SCAN korte hobe
EXPLAIN QUERY PLAN
SELECT * FROM transactions WHERE date = '2026-09-01';
-- Output: 'SCAN transactions' -- proti row check kore dekhte hobe

-- Ekhon index add kori
CREATE INDEX idx_transactions_date ON transactions(date);
CREATE INDEX idx_transactions_account ON transactions(account_id);

-- Age-r SAME query, ekhon plan check koro
EXPLAIN QUERY PLAN
SELECT * FROM transactions WHERE date = '2026-09-01';
-- Output: 'SEARCH transactions USING INDEX idx_transactions_date (date=?)'
-- -- ekhon pura table scan na kore shorashori index diye row khuje pay

-- account_id diye JOIN korle-o index kaje lage
EXPLAIN QUERY PLAN
SELECT * FROM transactions t JOIN accounts a ON t.account_id = a.id;
