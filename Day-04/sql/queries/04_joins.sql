-- 04_joins.sql  (Learn 2.6)
-- transactions.category ekta plain text. categories table-e sei category-r
-- extra info (group_type) ache. Dutoke jorar jonno JOIN lagbe.

-- INNER JOIN -- dutо table-e MATCH thakle-i row ashbe
SELECT
    t.date,
    t.amount,
    t.category,
    c.group_type
FROM transactions t
INNER JOIN categories c ON t.category = c.name
ORDER BY t.date;

-- LEFT JOIN -- transactions-er SOB row thakbe, category match na korleo
-- (categories-er dik theke NULL ashbe)
SELECT
    t.date,
    t.amount,
    t.category,
    c.group_type
FROM transactions t
LEFT JOIN categories c ON t.category = c.name
ORDER BY t.date;

-- ---------- JOIN mismatch dekhar jonno (Testing table #06) ----------
-- Ekta test transaction, jar category ('Entertainment') categories table-e NAI
-- (shudhu ei query-r moddei, permanent na)
WITH t AS (
    SELECT * FROM transactions
    UNION ALL
    SELECT 99, '2026-09-15', 'expense', 400, 'Entertainment', 'Movie night'
)
SELECT t.date, t.category, c.group_type, 'INNER' AS join_type
FROM t INNER JOIN categories c ON t.category = c.name
UNION ALL
SELECT t.date, t.category, c.group_type, 'LEFT'
FROM t LEFT JOIN categories c ON t.category = c.name
WHERE t.category = 'Entertainment';

-- Result: INNER JOIN-e 'Entertainment' row ekdom ashe na (match nai bole bad).
-- LEFT JOIN-e row thake, kintu group_type = NULL.
-- Decision: kokhon kon ta lagbe? Report-e "shob transaction dekhabo, category
-- na thakleo" -> LEFT JOIN. "Sudhu jegulor category confirm ache" -> INNER JOIN.

-- Group-wise total, joined
SELECT
    c.group_type,
    SUM(t.amount) AS total_amount
FROM transactions t
INNER JOIN categories c ON t.category = c.name
WHERE t.amount IS NOT NULL
GROUP BY c.group_type;