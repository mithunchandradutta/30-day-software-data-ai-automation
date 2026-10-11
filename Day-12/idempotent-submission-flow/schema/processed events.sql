-- Day 11-er table-er ekta bhalo version: ekhon "result"-o save kori,
-- jate retry-te ager-i result abar dewa jay.
CREATE TABLE processed_events (
    request_id  TEXT PRIMARY KEY,     -- <- database-level guarantee (Day 11-er moto)
    result      TEXT,                 -- ager result (ekhane transaction_id)
    received_at TEXT NOT NULL,
    status      TEXT NOT NULL
);