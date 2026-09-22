-- Exercise 03 -- GROUP BY & Aggregates  (Practice Lab)

-- Category onujayi total amount
SELECT category, SUM(amount) AS total_amount
FROM transactions
GROUP BY category;

-- Type onujayi total amount
SELECT type, SUM(amount) AS total_amount
FROM transactions
GROUP BY type;

-- Category-r average expense
SELECT category, AVG(amount) AS avg_amount
FROM transactions
WHERE type = 'expense'
GROUP BY category;

-- Category-r transaction count
SELECT category, COUNT(*) AS transaction_count
FROM transactions
GROUP BY category;