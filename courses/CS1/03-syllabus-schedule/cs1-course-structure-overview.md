# CS1 Course Structure Overview

**Student / admin one-pagers:** [CS1-course-structure.md](../CS1-course-structure.md) · [CS1-checkpoints.md](../CS1-checkpoints.md) · [CS1-minimum-passing-standard.md](../CS1-minimum-passing-standard.md) · [commit-message-guide.md](../commit-message-guide.md)

Official KLIS school calendar (2026–2027): [KLIS-School-Calendar-26-27.pdf](./KLIS-School-Calendar-26-27.pdf).

Semester 1 week-by-week pacing (draft): [cs1-pacing-guide.md](./cs1-pacing-guide.md).

Projects mapped to each module (板块 ↔ 项目): [cs1-projects-by-module.md](../05-project-book-crud/cs1-projects-by-module.md).

## Module 1. GitHub Foundations

### Skills

- Use GitHub website and GitHub Desktop for basic collaboration
- Understand repository, commit, push, pull, branch, and pull request
- Write clear commit messages

### Checkpoint

- Clone a repository using GitHub Desktop
- Make a change and commit it
- Push changes to GitHub
- Pull updates from GitHub
- Create a branch
- Open a pull request

### Project Task

- Create a personal repository and publish at least one update
- Complete one branch-based contribution and submit one pull request

### Evidence of Mastery

- Student can clone, commit, push, pull, branch, and open a PR
- Commit messages are meaningful
- Student can explain the basic collaboration workflow

---

## Module 2. HCI and Figma

### Skills

- Understand the purpose of needfinding
- Conduct interview, survey, and heuristic evaluation
- Critically evaluate an **existing** interface (app or website) and identify concrete usability problems
- Propose **targeted UI improvements** grounded in findings (not only greenfield concepts)
- Create a basic prototype in Figma
- Apply core design principles
- Recognize basic biases in research and design

### Checkpoint

- Conduct one interview
- Create one short survey
- Complete one heuristic evaluation of an existing interface
- Build one Figma prototype
- Explain design decisions using design principles

### Project Task

**Choose one track (unless you assign both at reduced depth):**

- **Track A — Course project (Book):** Investigate a user need related to the book project; create and revise a Figma prototype based on findings.
- **Track B — Redesign existing UI:** Pick a **real** product or flow (existing screens). Document the **current state**, run a **heuristic evaluation** (and light needfinding such as interview or survey if required), then produce a **Figma redesign** of the **key screens** that addresses the top issues—with short rationale tied to design principles.

### Evidence of Mastery

- Student can identify user needs and usability issues
- Student can create a prototype in Figma
- Student can explain design decisions clearly
- Student can identify possible bias in questions, assumptions, or design choices
- For **Track B**, student can show **before → after** intent (screenshots or linked reference of the current UI vs Figma) and justify **why** changes improve usability

---

## Module 3. LaTeX for Technical Communication

### Skills

- Use LaTeX to create a simple technical document
- Organize content with sections and lists
- Format text clearly
- Include simple code blocks, images, or tables
- Write short structured project explanations

### Checkpoint

- Create a one-page LaTeX document
- Use title, section, bullet points, and one image or code example

### Project Task

- Write a short design rationale or project summary in LaTeX

### Evidence of Mastery

- Student can create a clean and readable LaTeX document
- Document has clear structure and formatting
- Student can use LaTeX to communicate technical ideas, not just plain text

---

## Module 4. HTML / CSS / Bootstrap — Login Page (static)

### Skills

- Build a small **website login page** as a single focused deliverable: semantic HTML structure
- Style with CSS and Bootstrap utilities (typography, spacing, color, components)
- Use Bootstrap components and utility classes appropriate to forms and alerts
- Use Bootstrap layout tools to begin organizing the login screen

### Checkpoint

- Build a **responsive login page** using HTML, CSS, and Bootstrap (heading, username/email, password, submit; readable layout)

### Project Task

- Deliver the **static** version of the **course / book app login page**: valid structure, Bootstrap-based styling, and responsive behavior across at least two breakpoints

### Evidence of Mastery

- Login page structure is complete and semantic where it matters
- Layout is readable and organized on phone- and desktop-width viewports
- Bootstrap is used appropriately (not only custom CSS)
- Login form contains required elements (title, username or email, password, button)

---

## Module 5. Layout with Grid and Flexbox — Same Login Page (refined)

### Skills

- Use the Bootstrap **12-column grid** on the **same login page** (e.g. split branding vs form, or main column + side margin)
- Use **Flexbox** for vertical and horizontal alignment, spacing, and centering (e.g. full-viewport centering of a card, footer row)
- Choose Grid vs Flexbox **for parts of the login experience** based on layout needs

### Checkpoint

- **Refine** the login page using **Bootstrap Grid and Flexbox** together (clear use of rows/columns **and** flex alignment in the composition)

### Project Task

- **Upgrade** the Module 4 login page: polished responsive layout using grid + flex (optional: simple header/footer strip, “hero” branding column, or card panel—still **one login-focused page**)

### Evidence of Mastery

- Rows and columns are used correctly on the login page
- Flexbox is used appropriately (centering, distribution, or component alignment)
- The **same** login page is visually organized and responsive; scope stays login-centric rather than a separate multi-page marketing site

---

## Module 6. JavaScript DOM Manipulation — Dice Challenge

Use a small **Dice Challenge** app (single page, vanilla JS) so students practice DOM and events on a **bounded** UI before Next.js.

### Skills

- Select DOM elements and update content safely
- Add event listeners (e.g. roll, reset, change number of dice)
- Read input values (e.g. how many dice, optional rules)
- Change text and styles based on program state
- Show and hide content or toggle UI states (e.g. history panel, error messages)
- Perform simple validation (e.g. valid range for dice count)

### Checkpoint

- Working **Dice Challenge**: user action triggers random rolls; results are visible in the DOM; at least one control beyond a single “roll” button (e.g. reset, dice count, or total sum display)

### Project Task

- Build and submit a **Dice Challenge** page that meets **minimum scope** (adjust for your rubric):

  - **Roll** at least one die (values **1–6**) and **display** each outcome in the page (text or simple graphics)
  - Use **JavaScript only** (no framework) to update the DOM
  - Include **at least two** of: multiple dice, **sum** of faces, **reset**, configurable **number of dice** (with validation), short **roll history**, or disabled button while “rolling”

- **Stretch (optional):** apply the same DOM patterns to the **Module 4–5 login page** (e.g. client-side validation message)—not required if Dice Challenge is the sole graded artifact

### Evidence of Mastery

- Student can manipulate webpage content with JavaScript in response to user actions
- Event handling works correctly without breaking the page on repeated clicks
- State (last roll, sum, dice count, etc.) is reflected clearly in the UI
- Student can explain briefly how random values map to DOM updates

---

## Module 7. Next.js Frontend

### Skills

- Create a basic Next.js project
- Use page-based routing
- Create reusable components
- Pass data through props
- Build forms
- Fetch and render backend data

### Checkpoint

- Create a multi-page Next.js app
- Build components and render data on a page
- Submit form data from the frontend

### Project Task

- Build the frontend of the book project using Next.js

### Evidence of Mastery

- Student can build and organize multiple frontend pages
- Student can use components appropriately
- Student can connect frontend pages to API data

---

## Module 8. FastAPI Backend

### Skills

- Create a FastAPI project
- Build API endpoints
- Return JSON responses
- Implement CRUD operations for the book project
- Understand request and response flow

### Checkpoint

- Build CRUD endpoints for books

### Project Task

- Build the backend API for the book project

### Evidence of Mastery

- Student can create, read, update, and delete book data
- API routes work correctly
- Student can explain the purpose of each endpoint

---

## Module 9. PostgreSQL Integration

### Skills

- Understand tables, rows, columns, and primary keys
- Connect backend data to a real database
- Store book project data persistently
- Understand the relationship between API and database

### Checkpoint

- Connect the book project backend to PostgreSQL

### Project Task

- Replace temporary or in-memory storage with PostgreSQL-backed data

### Evidence of Mastery

- Data is stored persistently
- Student can explain the basic data model
- Student understands how backend endpoints connect to the database

---

## Module 10. Final Course Outcome

### Skills

- Combine design, frontend, backend, database, and collaboration workflow
- Build a simple full-stack web application

### Checkpoint

- Complete and present the final book project

### Project Task

- Deliver a simple full-stack book project with:

  - HCI research input
  - Figma prototype
  - HTML/CSS/Bootstrap **login page** with Grid/Flexbox-informed layout
  - JavaScript interactivity (forms / state in the Book app; builds on Module 6 DOM skills)
  - Next.js frontend
  - FastAPI backend
  - PostgreSQL data storage
  - GitHub workflow

### Evidence of Mastery

- Student can build a complete basic full-stack application
- Student can explain design and technical decisions
- Student can demonstrate a functional workflow from interface to database
