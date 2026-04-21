# KLIS CS Pathways

Public materials for **KLIS computer science pathways**, including **CS1** course structure, checkpoints, pacing, and GitHub workflow templates for students.

## CS1 — start here

| Document | Purpose |
|----------|---------|
| [CS1-course-structure.md](courses/CS1/CS1-course-structure.md) | Canonical syllabus: modules, skills, checkpoints, deliverables, passing bar, artifacts |
| [CS1-checkpoints.md](courses/CS1/CS1-checkpoints.md) | Student tick list per module checkpoint |
| [CS1-minimum-passing-standard.md](courses/CS1/CS1-minimum-passing-standard.md) | Course pass summary + links to full criteria |
| [commit-message-guide.md](courses/CS1/commit-message-guide.md) | Short guide for commits and PRs |

**More detail:** [cs1-course-structure-overview.md](courses/CS1/03-syllabus-schedule/cs1-course-structure-overview.md) · **Calendar & weeks:** [cs1-pacing-guide.md](courses/CS1/03-syllabus-schedule/cs1-pacing-guide.md) · **Projects vs modules:** [cs1-projects-by-module.md](courses/CS1/05-project-book-crud/cs1-projects-by-module.md) · **Competencies:** [cs1-required-competencies-checklist.md](courses/CS1/01-competencies-outcomes/cs1-required-competencies-checklist.md)

## Pathway (school-wide)

- [Pathway PDF](pathway/KLIS%20CS%20Pathway%20%26%20Prerequisites%20Bilingual(April%2020th).pdf) · [Overview infographic (SVG)](pathway/cs-pathway-overview-infographic.svg)

## GitHub templates (this repo)

- [Pull request template](.github/PULL_REQUEST_TEMPLATE.md)
- Issue form: [CS1 task](.github/ISSUE_TEMPLATE/cs1-task.yml)

---

## Public content review (maintainers)

**Automated scan:** No common secret patterns (`api_key`, private keys, `ghp_` tokens, etc.) were found in tracked Markdown/YAML. **PDFs** in `pathway/`, `courses/CS1/`, and root are curriculum / school calendar / readiness forms—confirm with your school before linking externally if any form contains personal data collection rules.

**Note:** `rebuild_pdfs.py` contains **hard-coded local paths** from another machine (Windows + user folder). It is **not** a secret, but you may want to remove or rewrite it for portability, or move it out of the public repo if unused.

Before each term, do a quick **manual** pass: open the repo in a private/incognito window and confirm files listed on GitHub match what you intend to share.
