# Git Notes: Pushing, Pulling, and Fixing a Rejected Push

Notes from a real problem: `git push` was rejected, `git pull --rebase` refused to run, and then hit a conflict. Every step is explained below.

---

## Core terms

| Term | Plain-English meaning |
|---|---|
| **Repository (repo)** | A project folder whose history git tracks. |
| **Commit** | A saved snapshot of your files, with a message describing the change. |
| **Local** | The copy on your Mac. |
| **Remote / origin** | The copy on GitHub. `origin` is the nickname for it. |
| **Branch** | A line of commits. Yours is `main`. |
| **Push** | Send your local commits up to GitHub. |
| **Pull** | Download commits from GitHub to your Mac. |
| **Staging** | Choosing which changes go into the next commit (`git add`). |
| **Working tree** | The files in your folder as they are right now. |
| **Rebase** | Replay your commits on top of the newest remote commits, giving a straight history. |
| **Conflict** | Git can't decide how to combine two changes and asks you to choose. |
| **HEAD** | The commit you're currently on. |
| **Detached HEAD** | HEAD isn't on a branch. This happens temporarily during a paused rebase. |

---

## The normal workflow

```bash
git status                       # what has changed?
git add fundamentals             # stage the changes
git commit -m "Add lesson 3"     # save a snapshot
git push                         # send it to GitHub
```

- `git status` is safe to run any time, and it's the first thing to try when confused.
- `git add` takes a file, a folder, or `.` / `-A` for everything. `-A` also stages deletions.
- `git commit -m "..."` needs a short message saying what changed.
- `git push` uploads your commits.

---

## What went wrong, step by step

### 1. Push rejected

```
! [rejected]  main -> main (fetch first)
hint: Updates were rejected because the remote contains work that you do not have locally.
```

- **Meaning:** GitHub had commits your Mac didn't. Git won't overwrite them, so it refuses the push.
- **Cause here:** files were changed or deleted on github.com in the browser (README, lesson files, `auth.log`).
- **Fix:** download the remote commits first with `git pull`, then push.

### 2. Pull refused

```
error: cannot pull with rebase: You have unstaged changes.
```

- **Meaning:** `git pull --rebase` needs a clean working tree, and `lesson2.py` had an uncommitted change (the deletion).
- **Fix:** commit the change, or stash it with `git stash`.

### 3. Conflict

```
CONFLICT (modify/delete): lesson2.py deleted in HEAD and modified in 3171ab0
```

- **Meaning:** one side deleted `lesson2.py`, and the other side changed it. Git can't pick a winner.
- **What "HEAD" means here:** during a rebase, HEAD is the remote history your commits are being replayed onto.
- **Fix:** tell git the deletion stands:

```bash
git rm lesson2.py
git rebase --continue
```

### 4. Detached HEAD message

```
fatal: You are not currently on a branch.
```

- **Meaning:** a rebase was paused, so git wasn't on `main` at that moment.
- **Fix:** nothing separate. It resolves when the rebase finishes.

### 5. Success

```
f8b1853..96a1c78  main -> main
nothing to commit, working tree clean
Your branch is up to date with 'origin/main'.
```

- `main -> main` means your local `main` was sent to the remote `main`.
- The two commit IDs show the range that was uploaded.
- "Working tree clean" means no uncommitted changes remain.

---

## Command reference

| Command | What it does |
|---|---|
| `git status` | Shows changed, staged, and untracked files |
| `git log --oneline` | Shows commit history, one line each |
| `git diff <file>` | Shows what changed in a file |
| `git add <path>` | Stages changes |
| `git commit -m "msg"` | Saves staged changes as a snapshot |
| `git push` | Uploads commits to GitHub |
| `git pull` | Downloads and merges remote commits |
| `git pull --rebase` | Downloads and replays your commits on top |
| `git stash` / `git stash pop` | Sets uncommitted changes aside, then restores them |
| `git rm <file>` | Deletes a file and stages the deletion |
| `git rebase --continue` | Resumes a paused rebase after resolving a conflict |
| `git rebase --skip` | Skips the current commit in a rebase |
| `git rebase --abort` | Cancels the rebase and returns to the previous state |
| `git restore <file>` | Discards uncommitted changes to a file (cannot be undone) |

---

## Errors and what they mean

| Message | Cause | Fix |
|---|---|---|
| `rejected ... (fetch first)` | Remote has commits you don't | `git pull --rebase`, then `git push` |
| `cannot pull with rebase: You have unstaged changes` | Uncommitted edits or deletions | Commit or stash them |
| `CONFLICT (modify/delete)` | One side edited a file the other deleted | Choose with `git rm` (keep deleted) or `git add` (keep the file) |
| `You are not currently on a branch` | Rebase is paused | Resolve the conflict and `git rebase --continue` |
| `nothing to commit, working tree clean` | Everything is already committed | Nothing to do |

---

## Habit that prevents this

Make changes in **one place**. If you edit on github.com, run `git pull` on your Mac before you start working. If you only edit locally, avoid the browser editor. Most rejected pushes come from changing the same repo in two places.

---

## Reading the log

```
96a1c78 (HEAD -> main, origin/main, origin/HEAD) Add lesson 3 conditions
f8b1853 Update 02_strings.py
9dbcb3e Delete README.md
```

- Newest commit is on top.
- `HEAD -> main` shows where you are, and `origin/main` shows where GitHub is. When they sit on the same commit, you're in sync.
- Messages like "Delete README.md" and "Update 02_strings.py" are the defaults GitHub writes for changes made in the browser.

---

## Interview-style explanation

> "I use git to version my projects. If a push is rejected because the remote has new commits, I pull with rebase to replay my work on top, resolve any conflicts, continue the rebase, and push. I check `git status` and `git log` along the way, and I keep my edits in one place so the histories don't diverge."

---

## Self-check questions

1. Why was the first push rejected?
2. What is the difference between `git add` and `git commit`?
3. Why did `git pull --rebase` refuse to run the first time?
4. What does a `modify/delete` conflict mean, and how did you resolve it?
5. How can you tell your local repo matches GitHub?

Answers: GitHub had commits your Mac lacked; `add` stages changes and `commit` saves a snapshot of what's staged; there were uncommitted changes in the working tree; one side changed a file the other deleted, resolved with `git rm` then `git rebase --continue`; `git status` says "up to date with origin/main" and the log shows `HEAD` and `origin/main` on the same commit.
