-- 00_schema.sql -- table structure (finance.db)
-- setup_db.py ei file poira table banay.

DROP TABLE IF EXISTs transactions;
DROP TABLE IF EXISTS categories;

-- Raw transactions, ekdom CSV-r moto -- ekhane KONO cleaning kora hoy nai.
-- Missing amount = NULL, duplicate row = duplicate thakbe.
-- Cleaning ekhon SQL query diye korbo (WHERE, GROUP BY...), Day 3-r moto
-- Python-e age theke clean kore rakhbo na

CREATE TABLE transactions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT, --'YYYY-MM-DD'
    type        TEXT, --'income' | 'expenses'
    amount      REAL, -- IT CAN BE NULL LIKE MISSING AMOUNT
    category    TEXT,
    description TEXT
);


-- Category lookup table -- JOIN practice-r jonno.
-- Ei table-e category-r extra info thake (budget group), ja transactions
-- table-e nai. Ei jonno-i JOIN lagbe -- normalization-er prothom glimpse (Day 5).

CREATE TABLE categories (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT UNIQUE,
    group_type  TEXT             -- 'Income' | 'Fixed Cost' | 'Variable Cost'
);