-- 06_indexes.sql  (Learn 2.7)
-- Index = boi-r index-er moto -- pura table na ghure shudhu shortcut diye
-- row khuje pawa jay. Trade-off: read druto hoy, kintu write-e ektu slow hoy
-- (index-o update lagbe), ar extra storage lage.
--
-- Kokhon lagbe: jei column diye ghono ghono WHERE/JOIN/GROUP BY hoy.
-- Proti column-e index deoya bhul -- "beshi index = beshi bhalo" na, karon
-- proti INSERT/UPDATE-e SOB index update korte hoy, tai onek index thakle
-- write dhire hoye jay ar shudhu shudhu storage nosto hoy.

CREATE INDEX idx_transactions_date    ON transactions(date);
CREATE INDEX idx_transactions_account ON transactions(account_id);

-- Extra (report-e category-wise GROUP BY ghono hoy, tai eta-o thik:)
CREATE INDEX idx_transactions_category ON transactions(category_id);
