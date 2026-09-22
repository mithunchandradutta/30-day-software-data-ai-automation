-- Exercise 03 -- Normalization  (Practice Lab)
-- Day 4-r flat table-e redundant data ki chilo, ar normalize korle ki hoy --
-- eta hate kore dekhar jonno.

-- Un-normalized (Day 4-r style) -- category-r naam BAR BAR repeat hocche
CREATE TABLE flat_transactions (
    id       INTEGER PRIMARY KEY,
    date     TEXT,
    amount   REAL,
    category TEXT       -- 'Food' 4 bar-i alada row-e likha ache
);

INSERT INTO flat_transactions VALUES
    (1, '2026-09-02', 500, 'Food'),
    (2, '2026-09-05', 150, 'Food'),
    (3, '2026-09-10', 200, 'Food'),
    (4, '2026-09-10', 200, 'Food');

-- Problem dekho: "Food" category-r naam "Foods" e change korte hole,
-- 4-ta row-i update korte hobe:
-- UPDATE flat_transactions SET category = 'Foods' WHERE category = 'Food';

-- Normalized version -- category ekbar-i categories table-e, transactions
-- shudhu id refer kore
CREATE TABLE categories (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE transactions_normalized (
    id          INTEGER PRIMARY KEY,
    date        TEXT,
    amount      REAL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO categories (name) VALUES ('Food');   -- id = 1

INSERT INTO transactions_normalized VALUES
    (1, '2026-09-02', 500, 1),
    (2, '2026-09-05', 150, 1),
    (3, '2026-09-10', 200, 1),
    (4, '2026-09-10', 200, 1);

-- Ekhon naam change korte hole shudhu EKTA row:
UPDATE categories SET name = 'Foods' WHERE id = 1;

-- 4-ta transaction-i notun naam pabe (JOIN diye dekhle):
SELECT t.id, t.date, t.amount, c.name AS category
FROM transactions_normalized t
JOIN categories c ON t.category_id = c.id;
