-- 03_grouping_aggregation.sql  (Learn 2.3, 2.4, 2.5)
-- ORDER BY, GROUP BY, aggregates (SUM/AVG/COUNT/MIN/MAX), HAVING

-- ===== ORDER BY =====

-- Top 5 largest transactions
SELECT * FROM transactions
ORDER BY amount DESC
LIMIT 5;

-- Top 5 smallest (SQLite-e NULL sobar age ashe ASC order-e)
SELECT * FROM transactions
WHERE amount IS NOT NULL
ORDER BY amount ASC
LIMIT 5;

-- Date onujayi sort
SELECT * FROM transactions
ORDER BY date ASC;

-- Multiple column sort
SELECT * FROM transactions
ORDER BY category ASC, amount DESC;

-- ===== GROUP BY + Aggregates =====
-- GROUP BY = pandas-r .groupby()-r SQL version. Split -> apply -> combine.

-- Total amount by category (expense-i dhorlam, karon Salary income)
SELECT category, SUM(amount) AS total_amount
FROM transactions
WHERE type = 'expense'
GROUP BY category
ORDER BY total_amount DESC;

-- Total amount by type
SELECT type, SUM(amount) AS total_amount
FROM transactions
GROUP BY type;

-- Average expense per category
SELECT category, AVG(amount) AS avg_amount
FROM transactions
WHERE type = 'expense'
GROUP BY category;

-- Transaction count per category
-- COUNT(amount) = amount na-thakle gonena, COUNT(*) = shob row gone (NULL soho)
SELECT category,
       COUNT(*)      AS row_count,
       COUNT(amount) AS non_null_count
FROM transactions
GROUP BY category;

-- MIN / MAX ekshathe
SELECT category,
       MIN(amount) AS smallest,
       MAX(amount) AS largest
FROM transactions
WHERE type = 'expense'
GROUP BY category;

-- ===== HAVING =====
-- WHERE row filter kore GROUP BY-r AGE, HAVING group filter kore AGGREGATE-r PORE.
-- Order: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY

-- Category jegulo-r total expense 500 er beshi
SELECT category, SUM(amount) AS total_amount
FROM transactions
WHERE type = 'expense'
GROUP BY category
HAVING SUM(amount) > 500;

-- Category jekhane 2-tar beshi transaction ache
SELECT category, COUNT(*) AS row_count
FROM transactions
GROUP BY category
HAVING COUNT(*) > 2;

-- Question: WHERE amount > 500 likhle ki HAVING SUM(amount) > 500-r shathe same hobe?
-- Na. WHERE row-by-row filter kore (grouping-r AGE), tai proti transaction
-- 500-r beshi kina dekhbe. HAVING pura category-r TOTAL 500-r beshi kina dekhbe
-- -- ekta category-r 3ta choto transaction mile 500 hote pare, WHERE oita dhorbe na.