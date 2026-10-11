# Branching Demo — step by step

A branch is an isolated workspace where you can experiment without
breaking `main`'s stable code. This demo uses the
`sql-transaction-analyzer` repo as an example, adding one small feature.

## 1. Create a new branch

```bash
cd sql-transaction-analyzer
git checkout -b feature/lowest-expense-query
```

`checkout -b` creates a new branch and switches to it in one step.
(In newer Git, `git switch -c feature/lowest-expense-query` does the same thing.)

## 2. Make a change and commit it

Say you add a new query to `queries/06_final_report.sql` — for example,
finding the lowest expense (this is a real change already made to that
project, so it works as a concrete example):

```bash
# after editing the file:
git add queries/06_final_report.sql run_report.py
git commit -m "feat: add lowest expense to final report"
```

## 3. Switch back to main and merge

```bash
git checkout main
git merge feature/lowest-expense-query
```

If there's no conflict, Git will do a "Fast-forward" merge automatically —
no manual work needed.

## 4. Delete the merged branch

```bash
git branch -d feature/lowest-expense-query
```

(`-d` only deletes a branch that's already merged. Deleting an unmerged
branch requires `-D`, which loses the commits — so use it carefully.)

## 5. Verify

```bash
git log --oneline --graph
```

The history will show that `feature/lowest-expense-query`'s commit is
now part of `main`.

---

## What a merge conflict looks like (awareness)

If `main` had also changed the same line in the meantime (say you and a
collaborator both edited the same function in `run_report.py`), Git can't
decide on its own which version to keep — the file will look like this:

```
<<<<<<< HEAD
total = sum(amounts)
=======
total = round(sum(amounts), 2)
>>>>>>> feature/lowest-expense-query
```

Everything from `<<<<<<< HEAD` to `=======` is `main`'s version.
Everything from `=======` to `>>>>>>>` is your branch's version.

Open the file by hand, decide which line(s) to keep, delete the
`<<<<<<<`, `=======`, `>>>>>>>` markers, then:

```bash
git add run_report.py
git commit
```

This isn't scary — Git hasn't lost any data, it's just asking you to
make the call.
