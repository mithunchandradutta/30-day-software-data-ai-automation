-- 01_accounts.sql  (Learn 2.1, 2.2)
-- accounts = ekta entity: bank/cash/mobile wallet, jekhane transaction hoy.
-- Ekhon porjonto shudhu "Main Account" thakbe (Day 4-r data-r jonno),
-- pore chaile multiple account add kora jabe -- schema-r jonno kono change lagbe na.

CREATE TABLE accounts (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,   -- proti table-r nijer unique id
    name TEXT NOT NULL,                       -- 'Main Account', 'BRAC Bank', 'Cash'
    type TEXT NOT NULL                        -- 'bank' | 'cash' | 'mobile wallet'
);
