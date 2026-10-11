# Example GitHub Issues (copy-paste these and create them by hand on GitHub)

Issue tracking is useful even on a solo project — it's a "don't have to
remember this from memory" list. When a bug or improvement comes to mind,
write it down as an issue instead of fixing it on the spot, then
prioritize later.

---

### Issue #1

**Title:** `fix: transactions.amount is nullable — deviates from original spec`
**Label:** `documentation`
**Body:**
```
The original Day 5 schema spec said `amount REAL NOT NULL`, but Day 4's
sample data has one row with a missing amount. Keeping NOT NULL would
have rejected that row during migration, breaking the "no data lost" rule.

Decision: `amount` is nullable, documented in the README.

Follow-up: once a real UI/API layer adds input validation, the DB-level
constraint could be tightened back to NOT NULL.
```
**Commit that closes it:**
```
docs: document amount NOT NULL deviation in schema README (Closes #1)
```

---

### Issue #2

**Title:** `enhancement: support multiple accounts in migration`
**Label:** `enhancement`
**Body:**
```
The current migration script (migrate_day4_data.sql) puts every
transaction on a default "Main Account", because Day 4's flat data had
no account concept at all.

The real Finance Tracker will have multiple accounts (BRAC Bank primary,
secondary, DPS savings...). The migration script should be made flexible
so it respects an account column in the CSV if present, and falls back
to a default account if not.
```

---

### Issue #3

**Title:** `bug: duplicate detection misses rows with a different description`
**Label:** `bug`
**Body:**
```
Duplicate fingerprint = date + amount + category (description is
excluded). This means two genuinely different transactions (e.g. two
separate ৳200 purchases the same day, with different descriptions) could
get flagged as duplicates if the fingerprint matches.

Fix idea: include description in the fingerprint, or check within a
short time window (e.g. same minute) instead.
```

---

## How to close one

If a commit message contains `Closes #<number>` (or `Fixes #<number>`,
`Resolves #<number>`), GitHub automatically closes that issue as soon as
the commit is merged/pushed to `main`. Example: use the commit message
above for Issue #1 in real life.

## Labels

| Label | When |
| --- | --- |
| `bug` | Something's broken or producing a wrong result |
| `enhancement` | A new feature or improvement |
| `documentation` | README/comment/doc-only change |
