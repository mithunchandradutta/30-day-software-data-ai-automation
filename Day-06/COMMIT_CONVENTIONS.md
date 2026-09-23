# Commit Message Conventions

## Prefixes

| Prefix | When to use it |
| --- | --- |
| `feat:` | Adding a new feature |
| `fix:` | Fixing a bug |
| `docs:` | Documentation/README changes only |
| `refactor:` | Restructuring code with the same behavior |
| `test:` | Adding or changing tests |
| `chore:` | Everything else (dependency bumps, moving files, `.gitignore` changes) |

## Rules

1. **One commit = one logical change.** Don't bundle two unrelated changes
   into one commit — it makes reviewing or reverting later much harder.
2. **The message should say WHAT changed and WHY**, not "updated stuff".
3. **Reading `git log` six months from now should make the change obvious.**

## Bad vs. good (real examples)

```
❌ "updated stuff"
❌ "fix"
❌ "final_v2_REAL"
❌ "more changes to analyzer"
```

```
✅ feat: add category grouping to transaction analyzer
✅ fix: handle missing amount values in transaction cleaner
✅ fix: enable foreign_keys pragma so invalid account_id is rejected
✅ docs: add ER diagram and migration notes to Day 5 README
✅ refactor: split cleaner.py load/clean logic out of main.py
✅ test: add 6 test cases for SQL duplicate + missing-amount detection
✅ chore: add .gitignore entry for generated finance.db
```

## Example commit history from your own Day 3–5 projects

These three projects already exist, so this is roughly what the commit
history would look like (use it as a reference while actually running
`git commit`):

**python-transaction-analyzer (Day 3)**
```
chore: initialize project structure and sample data
feat: add cleaner.py with missing-amount and duplicate handling
feat: add analyzer.py with category breakdown and monthly trend
feat: add main.py CLI report
test: add 6 test cases covering the Day 3 testing table
docs: add README with example input/output
```

**sql-transaction-analyzer (Day 4)**
```
chore: set up SQLite schema and seed categories table
feat: add filtering, grouping, and HAVING query examples
feat: add JOIN queries against categories table
feat: add CASE-based signed amount and size labels
feat: add final_report.sql matching Day 3's pandas output
test: add 6 test cases using an in-memory database
docs: document data-quality handling and deviations from Day 3
```

**financial-database-schema (Day 5)**
```
feat: add normalized schema (accounts, categories, transactions, loans, investments)
feat: add migration script for Day 4's 8 raw rows
feat: add build_schema.py and verify_report.py
test: add 6 test cases including foreign key and cascade behavior
docs: add ER diagram (Graphviz + Mermaid) and deviation notes
fix: make transactions.amount nullable to avoid losing the missing-amount row (Closes #1)
```

## Common commit mistakes

- One commit that touches 5 files, 3 unrelated fixes, and a typo — six
  months later it's impossible to tell which change the commit was
  actually for.
- Running `git add .` blindly — check `git status` and `git diff` first
  to see exactly what's about to be committed.
