# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is the **semester course repository** for KEA (Copenhagen School of Design and Technology) — IT Architecture, Agile Development & Cloud, Spring 2026. It is maintained by the teacher (`clbokea`) and contains all course material, exercises, and teaching resources. Students do not work in this repo directly; they work in their own group repositories.

The companion legacy project students work on is: [awsome_recipe_cookbook](https://github.com/cookbookio/awsome_recipe_cookbook)

## Repository Structure

Sessions are numbered folders (`01._introduction/`, `06._CI_github_actions/`, etc.) each containing:
- `README.md` — lesson plan with "Before Class", "Todays Teachings", "After Class" sections
- Markdown files for specific topics, tutorials, and exercises
- `exercises/` subfolder for hands-on assignments

Other key locations:
- `00._course_material/00._Meta_Course_Material/` — exam requirements, course overview, grading criteria
- `planleagning/` — teacher planning notes and topic outlines
- `emner/` — topic reference sheets and cheatsheets
- `groups.py` — student group registry with names, repos, tech stacks, and deployed endpoints
- `vibe-hackaton.py` — group registry for the CASE 1 vibe hackathon
- `14-18._CASE_1/` and `28-29._CASE_2/` — multi-session case/hackathon folders

## Semester Topics (in order)

1. Intro, SSH, legacy codebase, OpenAPI/Swagger
2. Framework selection, code migration (no Flask/Spring Boot allowed in student projects)
3–4. Linux, cross-platform tooling
5. Git branching strategies
6. GitHub Actions (CI)
7–8. Azure VM provisioning (`az` CLI, portal)
9–10. Continuous Delivery
12–13. Code quality: linting, static analysis, git hooks (Husky, pre-commit, pytest)
14–18. CASE 1: Vibe Hackathon
19. DevOps maturity assessment
20+. Nginx reverse proxy, load balancing, Kubernetes
28–29. CASE 2
30–33. Exam project

## Student Group Tracking (`groups.py`)

Each entry has: `name`, `gitLinks`, `backend`, `frontend`, `monitoring`, `stack`, `documentation`, `members`. Students submit PRs to add themselves. The `vibe-hackaton.py` file tracks hackathon-specific group data.

## Typical File Conventions

- Session READMEs follow a consistent template: Learning Goals → Before Class → Todays Teachings → After Class
- Assignment blocks use optional fields: `Type`, `Soft/Hard/No Deadline`, `Motivation`, `Part of the exam report`, `Requirement`
- Assets (images, diagrams) live in `assets_*/` subfolders within each session

## Exam Requirements Summary

Students must: use version control with a branching strategy, implement CI/CD (GitHub Actions or equivalent), deploy to cloud (Azure or similar), implement linting/testing, write an exam report, and present a live deployment. Framework must not be Flask or Spring Boot.
