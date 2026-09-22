-- 03_transactions.sql  (Learn 2.3, 2.4)
-- Age (Day 3/4): transactions(date, type, amount, category, description) --
--   category ekta plain TEXT chilo, ei jonno "Food" lekha 4 bar repeat hoyeche.
-- Ekhon: category ekta ID (foreign key) -- category-r naam ekbar-i categories
--   table-e ache, transactions shudhu oi ID-take refer kore. Eta-i normalization --
--   "Food" category-r naam change korte hole EKTA row update korlei hobe,
--   hajarta transaction row khunje khunje na.
--
-- account_id NOT NULL -- proti transaction KONO NA KONO account theke hote hobe.
-- category_id nullable -- category na dile-o transaction save howa uchit
--   (jemon: "Uncategorized" hisebe rekhe pore thik kora jabe).
--
-- amount REAL, NOT "NOT NULL" -- Doc-e amount NOT NULL bola ache, kintu Day 4-r
--   ekta row-e amount MISSING chilo (real-world-e eta hoyi). Migration-e
--   "8 row migrated, kono data হারায় নি" -- ei rule rakhte hole amount-e
--   NULL allow korte hoyeche. Missing amount ekhon-o SQL diye (`amount IS NULL`)
--   flag kora jay, shudhu row-tা bad porena.

CREATE TABLE transactions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id  INTEGER NOT NULL,
    category_id INTEGER,
    date        TEXT NOT NULL,
    type        TEXT NOT NULL,
    amount      REAL,
    description TEXT,
    FOREIGN KEY (account_id)  REFERENCES accounts(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
