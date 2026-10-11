-- 02_categories.sql  (Learn 2.2, 2.4)
-- Day 4-r categories table-i, ekhon "proper" entity hisebe.
-- name UNIQUE -- karon duita "Food" category thakle report bhul hoye jabe.

CREATE TABLE categories (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL UNIQUE,
    group_type TEXT                            -- 'Income' | 'Fixed Cost' | 'Variable Cost'
);
