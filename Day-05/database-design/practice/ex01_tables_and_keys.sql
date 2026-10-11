-- Exercise 01 -- Tables & Keys  (Practice Lab)
-- Run: sqlite3 :memory: < practice/ex01_tables_and_keys.sql
-- (:memory: -- test korার jonno, asol finance.db-te effect porbe na)

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

-- Test: NOT NULL kaj korche kina
INSERT INTO accounts (name, type) VALUES ('Main Account', 'bank');   -- OK
-- INSERT INTO accounts (type) VALUES ('bank');    -- eta fail korbe: name missing

SELECT * FROM accounts;
SELECT * FROM categories;
