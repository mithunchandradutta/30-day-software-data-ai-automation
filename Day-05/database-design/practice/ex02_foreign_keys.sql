-- Exercise 02 -- Foreign Keys  (Practice Lab)
-- Run: sqlite3 :memory: < practice/ex02_foreign_keys.sql
-- Dhyan dao: SQLite-e "PRAGMA foreign_keys = ON;" na dile FK check-i hoy na!

PRAGMA foreign_keys = ON;

CREATE TABLE accounts (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE categories (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL UNIQUE,
    group_type TEXT
);

CREATE TABLE transactions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id  INTEGER NOT NULL,
    category_id INTEGER,
    date        TEXT NOT NULL,
    type        TEXT NOT NULL,
    amount      REAL,
    description TEXT,
    FOREIGN KEY (account_id)  REFERENCES accounts(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO accounts (name, type) VALUES ('Main Account', 'bank');   -- id = 1

-- Invalid account_id (999 exist kore na) -- eta FAIL korar kotha
INSERT INTO transactions (account_id, date, type, amount)
VALUES (999, '2026-09-01', 'expense', 100);
-- Error: FOREIGN KEY constraint failed

-- Valid account_id (1) -- eta SUCCESS hobe
INSERT INTO transactions (account_id, date, type, amount)
VALUES (1, '2026-09-01', 'expense', 100);

SELECT * FROM transactions;
