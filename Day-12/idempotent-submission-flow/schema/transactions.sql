CREATE TABLE transactions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,
    type        TEXT NOT NULL,
    amount      REAL NOT NULL,
    description TEXT
);