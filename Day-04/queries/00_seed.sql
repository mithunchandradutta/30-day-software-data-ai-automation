-- 00_seed.sql -- categories table-e reference data
-- (transactions.csv theke ashe na, hate diye banano -- karon ei tai
--  extra business info jeta CSV-e chilo na, JOIN-er reason)

INSERT INTO categories (name, group_type) VALUES
    ('Salary',    'Income'),
    ('Bills',     'Fixed Cost'),
    ('Food',      'Variable Cost'),
    ('Transport', 'Variable Cost');

-- nb: 'Entertainment' category ekhane NAI.
-- Ex05_join.sql-e AMI ekta 'Entertainment' transaction ekhane add kore
-- DEKHBO LEFT JOIN kivabe unmatched row-o dhore rakhe, ar INNER JOIN
-- oita bad diye dey. ata shekar jonno ai test ta korlam.