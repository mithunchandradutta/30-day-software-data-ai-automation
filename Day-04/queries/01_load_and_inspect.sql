-- 01_load_and_inspect.sql  (Learn 2.1)
-- Data load hoyeche (setup_db.py diye). Ekhon inspect kori --
-- analysis shuru korar age ki ache dekhe newa.

-- Table structure dekho
PRAGMA table_info(transactions);

-- Koyta row ache?
SELECT COUNT(*) AS total_rows FROM transactions;

-- Prothom 5 row
SELECT * FROM transactions LIMIT 5;

-- Kotogula alada category ache?
SELECT DISTINCT category FROM transactions;

-- SELECT * (sob column) vs SELECT column1, column2 (nirdishto column)
SELECT date, category, amount FROM transactions LIMIT 5;

-- SQL declarative: "ki chai" bolo (SELECT ... WHERE ...),
-- "kivabe khuje ber korte hobe" (loop, index scan) SQL engine nijei thik kore.
-- Python-e (imperative) tumi step-by-step bole dao -- row by row loop, if condition...