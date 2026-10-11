-- Exercise 05 -- JOIN  (Practice Lab)
-- categories table setup_db.py diye already toiri hoyeche (queries/00_seed.sql)

-- Transaction + category name ekshathe
SELECT t.date, t.amount, t.category, c.group_type
FROM transactions t
INNER JOIN categories c ON t.category = c.name;

-- LEFT JOIN diye dekho: unmatched category thakle ki hoy?
-- (test korte 04_joins.sql-e 'Entertainment' example ache)
SELECT t.date, t.amount, t.category, c.group_type
FROM transactions t
LEFT JOIN categories c ON t.category = c.name;