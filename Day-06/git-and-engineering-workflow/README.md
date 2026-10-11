# Day 6 — Git + Engineering Workflow

> Day 6/30 — 30 Days of Software Engineering + Data + AI + Business Analytics
> by [Mithun Chandra Dutta](https://github.com/mithunchandradutta)

There's no new project code in this folder. Day 6's job was **how the code
gets tracked, reviewed, and shared** — not writing more of it. So this is
documentation only: workflow decisions, commit conventions, a branching
demo, and example issues.

## Structure Decision: Multi-repo (Option B)

The Day 3, 4, and 5 projects (pandas analyzer, SQL analyzer, database
schema) are already separate repositories:

- `python-transaction-analyzer` (Day 3)
- `sql-transaction-analyzer` (Day 4)
- `financial-database-schema` (Day 5)

So this is **multi-repo, not a monorepo** — following the doc's "Option B:
Separate repo per project (recommended for portfolio visibility)". Reasons:

- A recruiter or collaborator can open one repo and see exactly that
  project, instead of digging through 30 days' worth of files.
- Each project keeps its own README, its own `.gitignore`, its own commit
  history — clean and self-contained.
- `week-1-review/` (Day 7) acts as a small "index" repo — it links every
  day's repo in one place without duplicating any code.

## Files in this folder

| File | What it's for |
| --- | --- |
| `TOP-LEVEL-README.md` | A ready-to-use template for a GitHub profile README (`mithunchandradutta/mithunchandradutta`) or a "journey index" repo |
| `.gitignore` | The same `.gitignore` pattern used across every project — for consistency |
| `COMMIT_CONVENTIONS.md` | `feat:`/`fix:`/`docs:` convention, with real examples drawn from the actual Day 3–5 files |
| `BRANCHING.md` | A feature-branch walkthrough: create branch → change → merge into main → delete branch |
| `ISSUES.md` | 3 example GitHub Issues (title + label + body), plus how to close one with a commit |

## How to use this

1. Copy `TOP-LEVEL-README.md` into a GitHub profile README or a journey-index repo.
2. Check `.gitignore` against each existing repo — merge the patterns in if they're missing.
3. Read `COMMIT_CONVENTIONS.md` and use this style for every commit from now on.
4. Follow `BRANCHING.md` to actually run through a branch-and-merge once (useful for a video demo too).
5. Create the 3 issues from `ISSUES.md` by hand in GitHub's Issues tab on the Day 3/4/5 repos, label them, and close one with a linked commit.

## Testing table (from the Day 6 doc) — how to verify each one

| # | Test | How to check |
| --- | --- | --- |
| 01 | Clean Clone | `git clone` into a fresh folder and follow the README's "How to Run" — does it work? |
| 02 | Commit History | `git log --oneline` — does every message explain what changed? |
| 03 | Branch Merge | Follow `BRANCHING.md`'s demo — after merging, does `git log --oneline --graph` show a clear history? |
| 04 | .gitignore | `git status` — are `__pycache__/`, `.db`, `.env` files absent from "Untracked"? |
| 05 | Issue Linking | Push a commit with `(Closes #3)` in the message — does the linked GitHub Issue auto-close? |
| 06 | README Completeness | Send the repo to a friend — can they understand the purpose and run it within 2 minutes? |
