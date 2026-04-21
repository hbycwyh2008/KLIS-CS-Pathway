# CS1 Course Structure Overview

**Student / admin:** [CS1-course-structure.md](../CS1-course-structure.md) (canonical module specs) · [CS1-checkpoints.md](../CS1-checkpoints.md) · [CS1-minimum-passing-standard.md](../CS1-minimum-passing-standard.md) · [commit-message-guide.md](../commit-message-guide.md)  
This file keeps **extended Evidence of Mastery** and implementation notes; align checkpoints with **CS1-course-structure.md** when the two differ.

Official KLIS school calendar (2026–2027): [KLIS-School-Calendar-26-27.pdf](./KLIS-School-Calendar-26-27.pdf).

Semester 1 week-by-week pacing (draft): [cs1-pacing-guide.md](./cs1-pacing-guide.md).

Projects mapped to each module (板块 ↔ 项目): [cs1-projects-by-module.md](../05-project-book-crud/cs1-projects-by-module.md).

## Module 1. GitHub Foundations

### Skills

- Use GitHub website and GitHub Desktop for basic collaboration
- Understand repository, commit, push, pull, branch, and pull request
- Write clear commit messages

### Checkpoint

- Clone a repository
- Make one change
- Commit and push
- Create one branch
- Submit one pull request

### Project Task

- One personal repository update
- One branch-based contribution with PR

### Evidence of Mastery

- Student can clone, commit, push, pull, branch, and open a PR
- Commit messages are meaningful
- Student can explain the basic collaboration workflow

---

## Module 2. HCI and Figma

### Skills

- Explain the purpose of needfinding
- Conduct an interview; design a short survey; perform a heuristic evaluation
- Identify user needs and usability issues
- Create a prototype in Figma; explain design decisions using design principles
- Recognize basic biases in research and design
- *(Optional extension)* Critically evaluate an **existing** interface and propose targeted UI improvements (redesign track)

### Checkpoint

- One interview
- One survey
- One heuristic evaluation
- One Figma prototype
- One short design rationale

### Project Task

- HCI research summary
- Prototype draft
- Revision based on findings

### Evidence of Mastery

- Student can identify user needs and usability issues
- Student can create a prototype in Figma
- Student can explain design decisions clearly (alignment, contrast, consistency, hierarchy, spacing)
- Student can identify possible bias (e.g. leading questions, sampling bias, designer assumptions, confirmation bias)
- Redesign track (if assigned): **before → after** intent with rationale tied to design principles

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

## Module 5. Layout with Grid and Flexbox

### Skills

- Use the Bootstrap **12-column grid** system; place content into rows and columns correctly
- Use **Flexbox** for alignment, spacing, and centering
- Choose Grid vs Flexbox appropriately for each section

### Checkpoint

- One page section using **Bootstrap Grid**
- One page section using **Flexbox**

### Project Task

- Structured layout for the **project interface** (builds on the Module 4 static page)

### Evidence of Mastery

- At least one clearly identifiable **grid-based** section (rows/columns used correctly)
- At least one clearly identifiable **flex-based** section (alignment / spacing / centering)
- Overall layout is readable and responsive across viewports

---

## Module 6. JavaScript DOM Manipulation

### Skills

- Select DOM elements; add event listeners; read input values
- Change text or styles; show or hide elements
- Implement simple form validation

### Checkpoint

- Add interactivity to a **form-based page**

### Project Task

- **Interactive login page** or **interactive content section** (vanilla JavaScript; no framework)

### Evidence of Mastery

- Student can manipulate webpage content with JavaScript in response to user actions
- Event handling works correctly for repeated use
- DOM scope demonstrated: selection, click/input events, dynamic updates, simple validation

---

## Module 7. Next.js Frontend

### Skills

- Create a basic Next.js project; build multiple pages; use page-based routing
- Create reusable components; pass data through props; build forms
- Fetch data from an API; render API data; submit frontend data to the backend

### Checkpoint

- Multi-page frontend
- Reusable components
- One form
- One API fetch
- One frontend submission

### Project Task

- Build the frontend of the book project using Next.js

### Evidence of Mastery

- Student can build and organize multiple frontend pages
- Student can use components appropriately
- Student can connect frontend pages to API data

### Not required yet

- Advanced authentication; deep SSR/SSG comparison; middleware; advanced global state libraries

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

### Not required yet

- Advanced joins; indexing optimization; deep transaction or normalization theory

---

## Module 10. Final Course Outcome

### Skills

- Combine design, frontend, backend, database, and GitHub workflow
- Explain both **design** and **technical** decisions

### Checkpoint

- Final project presentation

### Project Task

- Deliver a simple full-stack book project with:

  - HCI research input
  - Figma prototype
  - HTML/CSS/Bootstrap layout
  - JavaScript interactivity
  - Next.js frontend
  - FastAPI backend
  - PostgreSQL storage
  - GitHub workflow evidence

### Evidence of Mastery

- Student can build a complete basic full-stack application
- Student can explain design and technical decisions
- Student can demonstrate a functional workflow from interface to database
