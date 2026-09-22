-- 06_final_report.sql
-- Day 3-r pandas report-er SAME output, ekhon shudhu SQL diye.
-- Approach: CTE (WITH ...) diye age "clean" data banai (missing bad,
-- duplicate-er ekta copy rakhi), tারপর তার উপর report-এর প্রতিটা অংশ বানাই।
-- run_report.py ei file-r query gulo chalie print-friendly report banay.

-- ---------- Step 1: cleaned data (valid + deduped) ----------
-- amount IS NOT NULL -> missing bad
-- id IN (MIN(id) per date+amount+category) -> duplicate-er PROTHOM copy-i thake
WITH valid AS (
    SELECT * FROM transactions WHERE amount IS NOT NULL
),
deduped AS (
    SELECT * FROM valid
    WHERE id IN (
        SELECT MIN(id) FROM valid GROUP BY date, amount, category
    )
)
SELECT * FROM deduped ORDER BY id;

-- ---------- Step 2: totals ----------
WITH valid AS (
    SELECT * FROM transactions WHERE amount IS NOT NULL
),
deduped AS (
    SELECT * FROM valid
    WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
)
SELECT
    SUM(CASE WHEN type = 'income'  THEN amount ELSE 0 END) AS total_income,
    SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS total_expense,
    SUM(CASE WHEN type = 'income'  THEN amount ELSE -amount END) AS balance
FROM deduped;

-- ---------- Step 3: category breakdown (% soho) ----------
WITH valid AS (
    SELECT * FROM transactions WHERE amount IS NOT NULL
),
deduped AS (
    SELECT * FROM valid
    WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
),
expense_totals AS (
    SELECT category, SUM(amount) AS total
    FROM deduped WHERE type = 'expense'
    GROUP BY category
)
SELECT
    category,
    total,
    ROUND(total * 100.0 / (SELECT SUM(total) FROM expense_totals), 1) AS percent
FROM expense_totals
ORDER BY total DESC;

-- ---------- Step 4: top & lowest expense ----------
WITH valid AS (
    SELECT * FROM transactions WHERE amount IS NOT NULL
),
deduped AS (
    SELECT * FROM valid
    WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
)
SELECT category, description, amount FROM deduped
WHERE type = 'expense'
ORDER BY amount DESC LIMIT 1;

WITH valid AS (
    SELECT * FROM transactions WHERE amount IS NOT NULL
),
deduped AS (
    SELECT * FROM valid
    WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
)
SELECT category, description, amount FROM deduped
WHERE type = 'expense'
ORDER BY amount ASC LIMIT 1;

-- ---------- Step 5: monthly trend ----------
-- Day 3-r monthly_trend() shudhu EXPENSE-r upor calculate kore (income na),
-- tai eta "oi mashe koto kharoch hoyeche" dekhay -- negative number.
WITH valid AS (
    SELECT * FROM transactions WHERE amount IS NOT NULL
),
deduped AS (
    SELECT * FROM valid
    WHERE id IN (SELECT MIN(id) FROM valid GROUP BY date, amount, category)
)
SELECT
    strftime('%Y-%m', date) AS month,
    SUM(-amount) AS net_change
FROM deduped
WHERE type = 'expense'
GROUP BY month;

-- ---------- Step 6: data quality (RAW table theke, deduped theke na) ----------
SELECT COUNT(*) AS missing_amounts FROM transactions WHERE amount IS NULL;

SELECT SUM(times_seen - 1) AS duplicate_rows FROM (
    SELECT COUNT(*) AS times_seen
    FROM transactions
    WHERE amount IS NOT NULL
    GROUP BY date, amount, category
    HAVING COUNT(*) > 1
);