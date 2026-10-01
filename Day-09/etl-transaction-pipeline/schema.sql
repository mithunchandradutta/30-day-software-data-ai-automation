-- schema.sql -- target tables this pipeline loads into
-- Same core idea as Day 5's normalized schema (accounts, categories,
-- transactions with foreign keys). loans/investments are left out here --
-- this project only loads transactions, so only the tables it actually
-- writes to are created.
--
-- Difference from Day 5: there, migration had to preserve raw, uncleaned
-- rows (so amount was made nullable). Here, Transform already filters out
-- malformed/missing-amount rows before Load ever runs -- by the time a row
-- reaches this schema it's already valid, so amount can stay NOT NULL.

CREATE TABLE IF NOT EXISTS accounts (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS categories (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS transactions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id  INTEGER NOT NULL,
    category_id INTEGER,
    date        TEXT NOT NULL,
    type        TEXT NOT NULL,
    amount      REAL NOT NULL,
    description TEXT,
    FOREIGN KEY (account_id)  REFERENCES accounts(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE INDEX IF NOT EXISTS idx_transactions_date    ON transactions(date);
CREATE INDEX IF NOT EXISTS idx_transactions_account ON transactions(account_id);