-- Transaction table (Day 5-er schema-r chhoto version)
CREATE TABLE transactions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,
    type        TEXT NOT NULL,      -- 'income' ba 'expense'
    amount      REAL NOT NULL,
    description TEXT
);