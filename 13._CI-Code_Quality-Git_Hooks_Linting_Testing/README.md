# CI - Code Quality - Git Hooks, Linting, Testing

We continue from the last session on code quality, focusing on setting up local linting and testing before each commit. We also include a short recap on how to set up a VM on Azure, update, upgrade, and install packages on the server to prepare it for deployment. Change the `SSH_HOST` secret on your GitHub repository to match your new VM. Run your workflow, admire your work, and teardown your VM afterward.

This session also provides an overview of what we covered so far and where you can find the information you need to follow the next week's assignment. 


## Learning Goals

## Before Class
Have a look at these files:

* [Infrastructure](https://github.com/cookbookio/awsome_recipe_cookbook/tree/linting/infrastructure)

Skim them and think about what are the scripts in the file(s) doing and what steps are described in the files.
Its not new stuff, but it is good to have a second look at it. 

## Today's Teachings

We will demo the process of creating a VM, updating it, installing docker on it, running a workflow on GitHub and looking at our deployed site. Then we will destroy it all and do it again, and again, and again.

* [Infrastructure](https://github.com/cookbookio/awsome_recipe_cookbook/tree/linting/infrastructure)

### Git Hooks
Last time we looked at adding linters to our [workflow on GitHub](https://github.com/cookbookio/awsome_recipe_cookbook/blob/linting/.github/workflows/linting.yml). Today we try to automatically lint or code before it is commited. This we do by using Git Hooks.

* [GitHooks](tutorial_githooks.md)
* [Precommit](tutorial_precommit.md)
* [PyTest Precommits](tutorial_pytest_precommit.md)

## After Class
For the one of you using Javascript you can have a look at these tools: 
* [Javascript - Husky, LintStaged](husky_lint_staged.md)
