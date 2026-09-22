-- Exercise 04 -- HAVING  (Practice Lab)

-- Category jegular total expense ekta threshold-r beshi
SELECT category, SUM(amount) AS total_amount
FROM transactions
WHERE type = 'expense'
GROUP BY category
HAVING SUM(amount) > 300;

-- Category jekhane N-tar beshi transaction ache
SELECT category, COUNT(*) AS transaction_count
FROM transactions
GROUP BY category
HAVING COUNT(*) > 1;