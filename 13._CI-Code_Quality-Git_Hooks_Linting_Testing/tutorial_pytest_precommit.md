# Tutorial: Running Pytest with Pre-commit

## Introduction
Pre-commit is a framework for managing Git hooks, and it can be used to run pytest automatically before each commit. This ensures that all tests pass before code is committed, improving code quality and reducing integration issues.

---

## Step 1: Install Pre-commit
First, install the `pre-commit` package using pip:

```bash
$ pip install pre-commit
```

---

## Step 2: Create a Configuration File
Create a `.pre-commit-config.yaml` file in the root of your repository. This file will configure pre-commit to run pytest before each commit:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
  - repo: local
    hooks:
      - id: pytest
        name: Run pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
```

---

## Step 3: Install the Hooks
Run the following command to install the hooks:

```bash
$ pre-commit install
```

This will set up the Git hooks in your `.git/hooks` directory.

---

## Step 4: Run the Hooks
To manually run the hooks on all files:

```bash
$ pre-commit run --all-files
```

---

## Step 5: Test the Hooks
1. Create a simple Python file with a test:
   ```python
   # test_example.py
   def test_example():
       assert 1 + 1 == 2
   ```

2. Stage the file:
   ```bash
   $ git add test_example.py
   ```

3. Attempt to commit:
   ```bash
   $ git commit -m "Test pytest pre-commit"
   ```

The pre-commit hook will run pytest and abort the commit if any tests fail.

---

## Step 6: Bypass the Hook (If Needed)
If you need to bypass the hook for a specific commit, use the `--no-verify` flag:

```bash
$ git commit --no-verify -m "Bypass hook"
```

---

## Pros and Cons of Using Pytest with Pre-commit

### Pros
- **Automated Testing**: Ensures tests are run before each commit.
- **Consistency**: All developers run the same tests.
- **Early Feedback**: Catches issues before they reach the repository.
- **Easy Setup**: Simple configuration and installation.

### Cons
- **Initial Setup**: Requires configuration and setup.
- **Dependency Management**: Requires Python and pip for installation.
- **Bypassable**: Developers can bypass hooks using the `--no-verify` flag.

---

## Advanced Configuration

### Customizing Pytest Options
You can customize pytest options in the `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: local
    hooks:
      - id: pytest
        name: Run pytest
        entry: pytest -v --tb=short
        language: system
        pass_filenames: false
        always_run: true
```

### Running Specific Tests
To run specific tests, modify the `entry` field:

```yaml
entry: pytest tests/test_example.py
```

---

## Conclusion
Using pytest with pre-commit ensures that all tests pass before code is committed, improving code quality and reducing integration issues. While it requires initial setup and Python, it provides a robust and easy-to-use framework for maintaining high standards of code.