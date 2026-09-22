-- 05_case_and_flags.sql  (Learn 2.7, 2.8 + Data quality)
-- CASE = SQL-er "if/else". Subqueries + data-quality flags.

-- ===== CASE: signed amount =====
-- Day 3 pandas: row["amount"] if row["type"]=="income" else -row["amount"]
SELECT
    date,
    type,
    amount,
    CASE
        WHEN type = 'income' THEN amount
        ELSE -amount
    END AS signed_amount
FROM transactions
WHERE amount IS NOT NULL;

-- ===== CASE: High / Medium / Low label =====
SELECT
    date,
    category,
    amount,
    CASE
        WHEN amount >= 1000 THEN 'High'
        WHEN amount >= 300  THEN 'Medium'
        ELSE 'Low'
    END AS size_label
FROM transactions
WHERE type = 'expense' AND amount IS NOT NULL
ORDER BY amount DESC;

-- ===== Subquery: average-er cheye boro expense =====
SELECT * FROM transactions
WHERE type = 'expense'
  AND amount > (SELECT AVG(amount) FROM transactions WHERE type = 'expense');

-- ===== Data quality: missing amounts =====
SELECT COUNT(*) AS missing_amounts
FROM transactions
WHERE amount IS NULL;

-- ===== Data quality: duplicate rows =====
-- fingerprint = date + amount + category (Day 3-r moto-i)
-- GROUP BY diye koybar eshechhe gono, HAVING diye 1-er beshi hole-i duplicate
SELECT date, amount, category, COUNT(*) AS times_seen
FROM transactions
WHERE amount IS NOT NULL
GROUP BY date, amount, category
HAVING COUNT(*) > 1;

-- Koyta EXTRA duplicate row ache (Day 3-r report-e ja dekhay -- "1 row"):
-- (COUNT(*) - 1) = koyta bari row, prottek duplicate group-e
SELECT SUM(times_seen - 1) AS duplicate_rows
FROM (
    SELECT COUNT(*) AS times_seen
    FROM transactions
    WHERE amount IS NOT NULL
    GROUP BY date, amount, category
    HAVING COUNT(*) > 1
);