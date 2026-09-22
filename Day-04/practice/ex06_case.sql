-- Exercise 06 -- CASE  (Practice Lab)

-- Signed amount column
SELECT
    date, type, amount,
    CASE WHEN type = 'income' THEN amount ELSE -amount END AS signed_amount
FROM transactions
WHERE amount IS NOT NULL;

-- High / Medium / Low label, amount threshold onujayi
SELECT
    date, category, amount,
    CASE
        WHEN amount >= 1000 THEN 'High'
        WHEN amount >= 300  THEN 'Medium'
        ELSE 'Low'
    END AS size_label
FROM transactions
WHERE type = 'expense' AND amount IS NOT NULL;