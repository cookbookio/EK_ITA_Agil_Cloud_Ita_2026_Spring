# Fork a repository with GitHub CLI

To fork a repository using the GitHub CLI (`gh`) from the command line.

---

## **1. Authenticate with GitHub**
Ensure you are logged in to your GitHub account via the `gh` CLI:
```bash
gh auth login
```
Follow the prompts to authenticate.

---

## **2. Fork the Repository**
Use the `gh repo fork` command to create a fork of the repository. Navigate to the directory where you want to clone the fork, or specify the `--clone` flag to clone it immediately.

```bash
gh repo fork OWNER/REPOSITORY --clone=true
```
Replace `OWNER/REPOSITORY` with the actual owner and repository name (e.g., `mistralai/mistral-docs`).

- The `--clone` flag will clone the fork to your local machine after forking it on GitHub.

---

## **3. Navigate to the Cloned Repository**
After forking and cloning, navigate into the repository directory:
```bash
cd REPOSITORY
```

---

## **Summary Table**


Fork a Repository with gh CLI


| Step | Command |
|------|---------|
| Authenticate with GitHub | `gh auth login` |
| Fork and clone the repository | `gh repo fork OWNER/REPOSITORY --clone=true` |
| Navigate to the repository | `cd REPOSITORY`|
