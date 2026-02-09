# Sync a fork from commandline
When you clone a repository from your GitHub account, you have a `remote` looking like this:

```
    git remote -v
    origin  https://github.com/YOUR_ORGANIZATION/FORKED_REPO.git (fetch)
    origin  https://github.com/YOUR_ORGANIZATION/FORKED_REPO.git (push)
```

To sync a fork with its upstream repository (the original) and pull down the new updates, follow these steps:

---

## **1. Add the Upstream Remote**
First, ensure your fork is linked to the original (upstream) repository.

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```
Replace `ORIGINAL_OWNER` and `ORIGINAL_REPOSITORY` with the actual owner and repository name.

---

## **2. Fetch the Latest Changes from Upstream**
Fetch the branches and their respective commits from the upstream repository.

```bash
git fetch upstream
```

---

## **3. Checkout Your Local Main Branch**
Make sure you are on your local main branch (or the branch you want to update).

```bash
git checkout main
```
Replace `main` with your branch name if it's different (e.g., `master` or `develop`).

---

## **4. Merge the Upstream Changes**
Merge the changes from the upstream repository into your local branch.

```bash
git merge upstream/main
```
Again, replace `main` with the branch name you want to sync with.

---

## **5. Push the Updates to Your Fork**
Push the merged changes to your fork on GitHub.

```bash
git push origin main
```

---

## **Using `gh` CLI (Optional)**
If you prefer using the `gh` CLI for some steps, you can use:

```bash
gh repo sync --source
```
This command will fetch and merge the upstream changes for you, but you still need to push the updates to your fork.

---

## **Summary Table**


Sync Fork Steps


| Step | Command |
|------|---------|
| Add upstream remote | `git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git` |
| Fetch upstream changes | `git fetch upstream` |
| Checkout local branch | `git checkout main` |
| Merge upstream changes | `git merge upstream/main` |
| Push to your fork | `git push origin main` |

---
