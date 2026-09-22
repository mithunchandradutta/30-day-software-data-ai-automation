-- 02_filtering.sql  (Learn 2.2)
-- WHERE = pandas-r boolean filtering-r SQL version.

-- Sob expense
SELECT * FROM transactions WHERE type = 'expense';

-- Sob income
SELECT * FROM transactions WHERE type = 'income';

-- Comparison operators + AND
SELECT * FROM transactions
WHERE type = 'expense' AND amount > 500;

-- OR
SELECT * FROM transactions
WHERE category = 'Food' OR category = 'Bills';

-- NOT
SELECT * FROM transactions
WHERE NOT type = 'income';

-- IN -- ekadhik value check (OR-er cheye porhte sohoj)
SELECT * FROM transactions
WHERE category IN ('Food', 'Transport');

-- BETWEEN -- range
SELECT * FROM transactions
WHERE amount BETWEEN 200 AND 1000;

-- LIKE -- pattern matching ('%' = jekono kisu, '_' = ekta character)
SELECT * FROM transactions
WHERE description LIKE '%electricity%';

SELECT * FROM transactions
WHERE description LIKE 'Bus%';       -- 'Bus' diye shuru

-- IS NULL / IS NOT NULL -- missing data khoja
-- Dhyan dao: amount = NULL kaj kore na, IS NULL lagbe
SELECT * FROM transactions WHERE amount IS NULL;
SELECT * FROM transactions WHERE amount IS NOT NULL;

-- Day 3-r pandas line:
--   df[(df["type"] == "expense") & (df["amount"] > 1000)]
-- SQL version:
SELECT * FROM transactions
WHERE type = 'expense' AND amount > 1000;