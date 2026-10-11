-- Exercise 01 -- SELECT & WHERE  (Practice Lab)
-- Run: sqlite3 data/finance.db < practice/ex01_select_where.sql
-- (age python setup_db.py chalie finance.db banao)

-- Sob expense transaction
SELECT * FROM transactions WHERE type = 'expense';

-- Sob income transaction
SELECT * FROM transactions WHERE type = 'income';

-- Amount 500-r beshi
SELECT * FROM transactions WHERE amount > 500;

-- Nirdishto category (IN diye)
SELECT * FROM transactions WHERE category IN ('Food', 'Bills');