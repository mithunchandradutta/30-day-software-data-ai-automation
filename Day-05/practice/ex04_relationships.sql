-- Exercise 04 -- Relationships (loans, investments, many-to-many)  (Practice Lab)

CREATE TABLE accounts (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL
);

-- loans -- accounts-r shathe one-to-many (ekta account-r multiple loan thakte pare)
CREATE TABLE loans (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id    INTEGER NOT NULL,
    principal     REAL NOT NULL,
    interest_rate REAL,
    start_date    TEXT NOT NULL,
    due_date      TEXT,
    status        TEXT DEFAULT 'active',
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

-- investments -- one-to-many (ekta account-r multiple investment thakte pare)
CREATE TABLE investments (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id      INTEGER NOT NULL,
    name            TEXT NOT NULL,
    invested_amount REAL NOT NULL,
    current_value   REAL,
    start_date      TEXT NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

-- ---------- (Optional) Many-to-many example ----------
-- Ekta investment ekadhik category-te porte pare (jemon: ekta stock
-- "Tech" ar "Growth" duita category-r under-e). Ei rokom many-to-many-r
-- jonno ekta junction/bridge table lagbe -- direct kono column diye
-- kora jay na, karon ekta side-e ekadhik value store kora jabe na.

CREATE TABLE categories (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE investment_categories (
    investment_id INTEGER NOT NULL,
    category_id   INTEGER NOT NULL,
    PRIMARY KEY (investment_id, category_id),   -- composite key -- duitar combination-i unique
    FOREIGN KEY (investment_id) REFERENCES investments(id),
    FOREIGN KEY (category_id)   REFERENCES categories(id)
);

-- Demo
INSERT INTO accounts (name, type) VALUES ('Main Account', 'bank');
INSERT INTO investments (account_id, name, invested_amount, start_date)
VALUES (1, 'Grameenphone Shares', 20000, '2026-01-15');
INSERT INTO categories (name) VALUES ('Tech'), ('Growth');
INSERT INTO investment_categories (investment_id, category_id) VALUES (1, 1), (1, 2);

-- Ekta investment-r shob category dekho
SELECT i.name, c.name AS category
FROM investments i
JOIN investment_categories ic ON i.id = ic.investment_id
JOIN categories c ON ic.category_id = c.id;
