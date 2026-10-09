-- Day 11-er sobcheye important table.
-- request_id PRIMARY KEY = database nijei bole dey: "ekoi request_id 2 bar thakte parbe na"
CREATE TABLE processed_events (
    request_id     TEXT PRIMARY KEY,
    transaction_id INTEGER,
    received_at    TEXT NOT NULL,
    status         TEXT NOT NULL
);