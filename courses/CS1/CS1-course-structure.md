# CS1 Course Structure

Related: [03-syllabus-schedule/cs1-pacing-guide.md](./03-syllabus-schedule/cs1-pacing-guide.md) · [05-project-book-crud/cs1-projects-by-module.md](./05-project-book-crud/cs1-projects-by-module.md) · [CS1-checkpoints.md](./CS1-checkpoints.md)

## Course Positioning

CS1 focuses on foundational web development, introductory full-stack integration, design thinking, and collaboration workflow. Students will learn how to move from user needs and interface design to frontend development, backend API construction, database integration, and basic GitHub collaboration.

The course emphasizes:

- GitHub workflow habits
- HCI and design reasoning
- frontend development
- introductory full-stack development
- basic technical communication

---

## 1. Course Modules Overview

### Module 1. GitHub Foundations

#### Core Skills

- clone a repository using GitHub Desktop
- make local changes
- create clear commits
- push changes to GitHub
- pull updates from GitHub
- create and switch branches
- open a pull request

#### Checkpoint

- clone a repository
- make one change
- commit and push
- create one branch
- submit one pull request

#### Deliverable

- one personal repository update
- one branch-based contribution with PR

#### Notes

This module focuses on the minimum collaboration workflow only.  
Conflict resolution, rebase, and advanced Git features are not required at this stage.

---

### Module 2. HCI and Figma

#### Core Skills

- explain the purpose of needfinding
- conduct an interview
- design a short survey
- perform a heuristic evaluation
- identify user needs and usability issues
- create a prototype in Figma
- explain design decisions using design principles
- recognize basic biases in research and design

#### Checkpoint

- one interview
- one survey
- one heuristic evaluation
- one Figma prototype
- one short design rationale

#### Deliverable

- HCI research summary
- prototype draft
- revision based on findings

#### Design Principles Focus

- alignment
- contrast
- consistency
- hierarchy
- spacing

#### Biases Focus

- leading questions
- sampling bias
- designer assumptions
- confirmation bias

---

### Module 3. LaTeX for Technical Communication

#### Core Skills

- create a simple LaTeX document
- use sections and bullet points
- format text clearly
- include one code block, image, or table
- write a short technical explanation

#### Checkpoint

- one-page LaTeX document

#### Deliverable

- short design rationale or project summary written in LaTeX

#### Notes

LaTeX is used as a communication tool, not as a full typography course.

---

### Module 4. HTML / CSS / Bootstrap

#### Core Skills

- build webpage structure with HTML
- style a page with CSS
- use Bootstrap components and utility classes
- create a functional login page

#### Checkpoint

- responsive login page

#### Deliverable

- first static frontend page

#### Bootstrap Scope

- navbar
- form
- button
- card
- grid layout

---

### Module 5. Layout with Grid and Flexbox

#### Core Skills

- use the Bootstrap 12-column grid system
- place content into rows and columns correctly
- use Flexbox for alignment, spacing, and centering
- choose between Grid and Flexbox appropriately

#### Checkpoint

- one page section using Bootstrap Grid
- one page section using Flexbox

#### Deliverable

- structured layout for the project interface

---

### Module 6. JavaScript DOM Manipulation

#### Core Skills

- select DOM elements
- add event listeners
- read input values
- change text or styles
- show or hide elements
- implement simple form validation

#### Checkpoint

- add interactivity to a form-based page

#### Deliverable

- interactive login page or interactive content section

#### DOM Scope

- element selection
- click events
- input handling
- dynamic updates
- simple validation

---

### Module 7. Next.js Frontend

#### Core Skills

- create a basic Next.js project
- build multiple pages
- use page-based routing
- create reusable components
- pass data through props
- build forms
- fetch data from an API
- render API data
- submit frontend data to the backend

#### Checkpoint

- multi-page frontend
- reusable components
- one form
- one API fetch
- one frontend submission

#### Deliverable

- frontend of the book project

#### Scope

- project setup
- routing
- components
- props
- forms
- fetch/render
- submit data

#### Not Required Yet

- advanced authentication
- deep SSR/SSG comparison
- middleware
- advanced state management

---

### Module 8. FastAPI Backend

#### Core Skills

- create a FastAPI project
- define API endpoints
- return JSON responses
- implement CRUD operations
- explain request/response flow

#### Checkpoint

- CRUD endpoints for books

#### Deliverable

- backend API for the book project

#### CRUD Scope

- Create book
- Read all books / one book
- Update book
- Delete book

---

### Module 9. PostgreSQL Integration

#### Core Skills

- explain table, row, and column
- explain primary key
- connect backend data to PostgreSQL
- persist book project data
- explain the relationship between API and database

#### Checkpoint

- connect the book project backend to PostgreSQL

#### Deliverable

- persistent backend data storage

#### Scope

- simple schema
- basic data persistence
- API-to-database connection

#### Not Required Yet

- advanced joins
- indexing optimization
- transaction theory
- deep normalization theory

---

### Module 10. Final Project

#### Core Skills

- combine design, frontend, backend, database, and GitHub workflow
- explain both design decisions and technical decisions

#### Checkpoint

- final project presentation

#### Deliverable

A simple full-stack book project that includes:

- HCI research input
- Figma prototype
- HTML/CSS/Bootstrap layout
- JavaScript interactivity
- Next.js frontend
- FastAPI backend
- PostgreSQL storage
- GitHub workflow evidence

---

## 2. Minimum Passing Standard

A student passes CS1 only if they can:

- build a responsive login page
- use Bootstrap Grid and Flexbox appropriately
- manipulate webpage content with JavaScript
- create a simple multi-page Next.js frontend
- implement CRUD endpoints in FastAPI
- connect project data to PostgreSQL
- use GitHub Desktop for clone, commit, push, pull, branch, and PR
- explain at least some design decisions using HCI findings and design principles

---

## 3. Required Student Artifacts

Each student or group should produce:

- GitHub repository activity
- commit history with meaningful commit messages
- at least one pull request
- one HCI research summary
- one Figma prototype
- one LaTeX technical write-up
- one static frontend page
- one interactive frontend page
- one Next.js frontend
- one FastAPI backend
- one PostgreSQL-backed project

---

## 4. Suggested GitHub Requirements

### Commit Message Expectation

Students should write clear commit messages, for example:

- Add login page structure
- Update survey questions
- Build book list component
- Fix delete book endpoint

Avoid vague messages such as:

- update
- final
- done
- change file

### Minimum GitHub Workflow

- clone
- edit
- commit
- push
- pull
- branch
- PR

More detail: [commit-message-guide.md](./commit-message-guide.md)

---

## 5. HCI Output Format

Each HCI task should include:

- Goal
- Method
- Key Findings
- Design Changes
- Bias Reflection

This keeps HCI work concrete and connected to the project.

---

## 6. Teacher Notes

### Keep the course focused

CS1 is not intended to become:

- a full Git course
- a deep HCI theory course
- a complete Next.js framework course
- a database theory course
- a DevOps course

### The core course flow is

GitHub → HCI/Figma → LaTeX → HTML/CSS/Bootstrap → Grid/Flexbox → JavaScript → Next.js → FastAPI → PostgreSQL → Final Project

Extended competencies checklist: [01-competencies-outcomes/cs1-required-competencies-checklist.md](./01-competencies-outcomes/cs1-required-competencies-checklist.md) · Rubric-level detail: [03-syllabus-schedule/cs1-course-structure-overview.md](./03-syllabus-schedule/cs1-course-structure-overview.md)
