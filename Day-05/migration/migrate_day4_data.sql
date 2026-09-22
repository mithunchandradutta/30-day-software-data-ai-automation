-- migrate_day4_data.sql
-- Day 4-r flat transactions.csv (8 row, RAW -- missing amount + duplicate soho)
-- eikhane HUBOHU migrate kora hocche notun normalized schema-te.
--
-- Lokkho koro: eita "clean kore migrate" na -- Day 3/4-e data quality flag
-- kora hoyeche SQL diye (WHERE amount IS NULL, GROUP BY+HAVING), delete kora hoyni.
-- Tai ekhane-o 8-r 8 row-i migrate hocche -- "kono data হারায় নি" (Test #05)।
--
-- Proti INSERT-e category_id ar account_id ber kora hocche subquery diye,
-- 03_transactions.sql-r foreign key column-e SOJA "Salary" lekha jabe na --
-- oi text-take age categories table-e giye id khunje ante hobe. Eta-i
-- referential integrity: shudhu VALID id-i store hoy.

INSERT INTO transactions (account_id, category_id, date, type, amount, description)
VALUES
    (
        (SELECT id FROM accounts WHERE name = 'Main Account'),
        (SELECT id FROM categories WHERE name = 'Salary'),
        '2026-09-01', 'income', 5000, 'September salary'
    ),
    (
        (SELECT id FROM accounts WHERE name = 'Main Account'),
        (SELECT id FROM categories WHERE name = 'Food'),
        '2026-09-02', 'expense', 500, 'Lunch with friends'
    ),
    (
        (SELECT id FROM accounts WHERE name = 'Main Account'),
        (SELECT id FROM categories WHERE name = 'Transport'),
        '2026-09-03', 'expense', 300, 'Bus + rickshaw'
    ),
    (
        (SELECT id FROM accounts WHERE name = 'Main Account'),
        (SELECT id FROM categories WHERE name = 'Food'),
        '2026-09-05', 'expense', 150, 'Groceries'
    ),
    (
        (SELECT id FROM accounts WHERE name = 'Main Account'),
        (SELECT id FROM categories WHERE name = 'Bills'),
        '2026-09-07', 'expense', 1200, 'Internet + electricity'
    ),
    (
        (SELECT id FROM accounts WHERE name = 'Main Account'),
        (SELECT id FROM categories WHERE name = 'Food'),
        '2026-09-10', 'expense', NULL, 'Missing amount'
    ),
    (
        (SELECT id FROM accounts WHERE name = 'Main Account'),
        (SELECT id FROM categories WHERE name = 'Food'),
        '2026-09-10', 'expense', 200, 'Snacks'
    ),
    (
        (SELECT id FROM accounts WHERE name = 'Main Account'),
        (SELECT id FROM categories WHERE name = 'Food'),
        '2026-09-10', 'expense', 200, 'Snacks'
    );
