-- seed_accounts_categories.sql
-- Migration-r AGE, reference data (account + categories) thaka lagbe --
-- karon transactions-r account_id / category_id ei table gulor id refer korbe.

INSERT INTO accounts (name, type) VALUES
    ('Main Account', 'bank');
    -- Day 4-r flat data-te kono account column chilo na, tai shob transaction
    -- ekta default "Main Account"-e migrate hocche. Pore multiple account
    -- add korle notun transaction gulo alada account_id-r shathe link hobe.

INSERT INTO categories (name, group_type) VALUES
    ('Salary',    'Income'),
    ('Bills',     'Fixed Cost'),
    ('Food',      'Variable Cost'),
    ('Transport', 'Variable Cost');
