# CS1 Pacing Guide (Semester 1)

This guide maps **CS1 modules** to **calendar weeks** for **Semester 1** using the KLIS 2026–2027 school calendar. Treat it as a working draft: adjust for your **A/B rotation**, **90-minute block count per week**, and **assessment windows**.

**KLIS schedule model (as you described):** classes follow an **A day / B day** rotation; each CS meeting is **90 minutes**. Students are **not** in CS every weekday—plan each week in **CS class blocks**, not “five CS days.”

- Official calendar: [KLIS-School-Calendar-26-27.pdf](./KLIS-School-Calendar-26-27.pdf)  
- Module detail (skills, checkpoints, evidence): [cs1-course-structure-overview.md](./cs1-course-structure-overview.md)

---

## Assumptions (edit to match your schedule)

1. **Scope:** CS1 Semester 1 runs from **first day of school (2026-08-24)** through **S1 grades closing (2027-01-22)**. Second semester is not mapped here.  
2. **Calendar:** Blackout dates follow the PDF (national holidays, Thanksgiving, winter break, one PTC no-school day). **Halloween** and **early-release** days are noted as lighter-touch class days, not full blackouts.  
3. **Standing commitment:** **Regular Wednesday after-school faculty meeting or PD** — consider lighter new content or lighter homework due **Thursday** that week.  
4. **A/B + 90 minutes:** Each **CS class = one 90-minute block**. CS does **not** meet every weekday. The week-by-week table includes **two computed counts** for blocks per week: **CS on A-days** and **CS on B-days** (see **How the counts are calculated** below). **Circle the one that matches your master schedule** (or overwrite with official day labels if KLIS uses a different rule after breaks).  
5. **School-wide contact days (not CS-specific):** About **91** Mon–Fri **school** days fall in this window after removing full holiday blackouts (rough count). That helps you see **short weeks**; it does **not** mean 91 CS periods. With the calendar-based A/B model below, a **full** five-day school week usually shows **2 or 3** CS blocks when CS is tied to **one** day-type only.  
6. **Book project:** One continuous thread from **Module 4** (static UI) through **Module 10** (integration + presentation).

### How the `CS blocks` counts are calculated (S1)

- **Blackout (no school)** matches the KLIS PDF used elsewhere in this repo: **2026-09-25–10-04**, **2026-11-06** (PTC), **2026-11-26–29** (Thanksgiving), **2026-12-19–2027-01-03** (winter break). **Early-release** days still count as **one** school day and **one** block if that weekday is a CS day.  
- **Day type:** **2026-08-24 = A day**. Each **calendar** date advances the letter: `A, B, A, B, …` by `(date − 2026-08-24).days mod 2` (weekends and holidays **still advance** the pattern, as if the cycle never pauses).  
- **Per week:** For each **Monday–Friday** date in that calendar week that is (a) inside **2026-08-24 … 2027-01-22**, (b) **not** in a blackout, count **1** block if that date is an **A** (column *CS on A*) or a **B** (column *CS on B*).  
- **Semester 1 totals (this model):** **45** blocks if CS is scheduled on **A-days** only; **46** blocks if on **B-days** only. If your registrar **freezes** A/B across breaks differently, replace the two columns for the weeks after each long break.

### If your school uses “instructional-day” A/B instead

Some schools advance A/B **only on days students attend**. That can **diverge** from the table after long breaks. In that case, keep the **module pacing** and **M–F school days** columns, but replace **CS on A / CS on B** with counts from the **official cycle calendar**.

---

## Semester 1 at a glance

| Phase | S1 weeks (approx.) | Modules | Book project thread |
|------|-------------------|---------|---------------------|
| Setup & design | 1–5 (+ holiday week 6) | 1–3 | Choose project scope; capture needs; write short rationale |
| Static web | 7–10 | 4–5 | Static **login page** (M4); **grid + flex sections** on project UI (M5) |
| Client interactivity | 11–14 | 6 | **Form-based JS** (interactive login or content section) |
| Application frontend | 15–17 | 7 | Next.js book UI; list/detail/forms |
| Backend & data | 20–21 | 8–9 | FastAPI CRUD; PostgreSQL persistence |
| Integration & close | 22 | 10 | Full stack demo + design/tech explanation |

Weeks **18–19** are **winter break** (no classes): optional async polish or catch-up reading only.

---

## Week-by-week pacing

**Legend**

- **M–F school days** = weekdays **school is in session** that week (any subject). Used to spot **short weeks** and holidays.  
- **CS on A / CS on B** = number of **90-minute CS blocks** that week **if** CS is timetabled only on **A-type** or only on **B-type** days, using the **calendar-based** A/B rule in *How the counts are calculated*. Pick the column that matches your section. If CS meets **more than once per cycle** (e.g. both A and B), **do not** use these two columns as-is—use the **registrar / master schedule** counts instead.  
- Plan in-class work per **actual block**, not per calendar day. **Early-release** days still count as one block if that day is a CS day.

| S1 week | Week of (Mon–Fri) | M–F school days | CS on A (90 min) | CS on B (90 min) | Calendar / school notes | Primary module(s) | Focus & suggested deliverables (scale to your CS blocks) | Book project milestone |
|--------:|-------------------|----------------:|-----------------:|-----------------:|-------------------------|-------------------|--------------------------------|------------------------|
| 1 | 2026-08-24 – 2026-08-28 | 5 | 3 | 2 | First day of school | **1** GitHub | Repos, clone, local edit, commit, push, pull; commit message norms | Repo created; project folder convention agreed |
| 2 | 2026-08-31 – 2026-09-04 | 5 | 2 | 3 | | **1** GitHub | Branching, PR workflow, peer or teacher review habit | **M1 project task:** personal repo + one branch-based PR |
| 3 | 2026-09-07 – 2026-09-11 | 5 | 3 | 2 | | **2** HCI / Figma | Needfinding goals; ethics of interviews; draft interview guide | Problem statement + target user for book app |
| 4 | 2026-09-14 – 2026-09-18 | 5 | 2 | 3 | | **2** HCI / Figma | Conduct interview; short survey draft; heuristic eval plan | **Checkpoint:** interview done; survey live or drafted |
| 5 | 2026-09-21 – 2026-09-25 | 4 | 2 | 2 | **2026-09-25** starts Mid-Autumn + National Day holiday | **2** HCI / Figma | Heuristic evaluation; Figma low-fi → key screens | **M2 project task:** Figma prototype v1 tied to book flows |
| 6 | 2026-09-28 – 2026-10-02 | 0 | 0 | 0 | **Holiday (no school)** | — | Optional: watch async, polish Figma, no graded new topic | Optional prototype revision |
| 7 | 2026-10-05 – 2026-10-09 | 5 | 3 | 2 | Return from holiday | **3** LaTeX + **4** start | One-page LaTeX (title, sections, list, image or code); HTML skeleton | **M3 task:** short design rationale or summary in LaTeX |
| 8 | 2026-10-12 – 2026-10-16 | 5 | 2 | 3 | | **4** HTML / CSS / Bootstrap | Semantic structure; Bootstrap basics; build **static login page** shell | Static **login page** structure (single-page deliverable) |
| 9 | 2026-10-19 – 2026-10-23 | 5 | 3 | 2 | | **4** HTML / CSS / Bootstrap | Responsive login; utilities; readability; form controls | **M4 checkpoint:** responsive **login page** |
| 10 | 2026-10-26 – 2026-10-30 | 5 | 2 | 3 | **2026-10-31** Halloween event (calendar) | **5** Grid / Flexbox | Build **one Bootstrap Grid section** + **one Flexbox section** on the project UI | **M5 checkpoint:** grid section + flex section both visible |
| 11 | 2026-11-02 – 2026-11-06 | 4 | 2 | 2 | **2026-11-03** Q1 / progress report; **2026-11-06** PTC (no school) | **5** → **6** | Integrate layout into project pages; introduce DOM selection + **form** events | **Structured layout** deliverable shaping up |
| 12 | 2026-11-09 – 2026-11-13 | 5 | 2 | 3 | | **6** JavaScript DOM | Event listeners; read inputs; update text/styles on **form-based page** | Interactivity on **login** or assigned content section |
| 13 | 2026-11-16 – 2026-11-20 | 5 | 3 | 2 | | **6** JavaScript DOM | Simple validation; show/hide messages | **M6 checkpoint:** interactive **form-based** page works end-to-end |
| 14 | 2026-11-23 – 2026-11-27 | 3 | 1 | 2 | **Thanksgiving** (Thu–Fri off per calendar) | **6** (catch-up) → **7** preview | Polish JS UX; buffer; optional Next.js setup video | M6 deliverable **submitted** or final fixes |
| 15 | 2026-11-30 – 2026-12-04 | 5 | 3 | 2 | | **7** Next.js | `create-next-app`; pages routing; components; props | Next shell mirroring static pages |
| 16 | 2026-12-07 – 2026-12-11 | 5 | 2 | 3 | | **7** Next.js | Forms; `fetch` to API (mock or live); render lists | Book list page from API (mock OK early) |
| 17 | 2026-12-14 – 2026-12-18 | 5 | 3 | 2 | **2026-12-18** Christmas & New Year event (**early release**) | **7** Next.js | Submit data to backend; error states; loading | **M7 checkpoint:** multi-page app + form submit path |
| 18 | 2026-12-21 – 2026-12-25 | 0 | 0 | 0 | **Winter break (no school)** | — | Optional polish only | Optional: README, screenshots |
| 19 | 2026-12-28 – 2027-01-01 | 0 | 0 | 0 | **Winter break (no school)** | — | Optional polish only | — |
| 20 | 2027-01-04 – 2027-01-08 | 5 | 2 | 3 | Return from break | **8** FastAPI | Project layout; routes; JSON; in-memory or temp store first | **M8 checkpoint:** CRUD routes for books (contract stable) |
| 21 | 2027-01-11 – 2027-01-15 | 5 | 3 | 2 | | **8–9** FastAPI + **PostgreSQL** | DB connection; models/migrations (as you teach); swap persistence | **M9 project task:** Postgres-backed books |
| 22 | 2027-01-18 – 2027-01-22 | 5 | 2 | 3 | **2027-01-22** S1 grades closing (**early release**) | **10** Final | Integration testing; demo script; rubric self-check; presentations | **Final:** full-stack demo + explanation |

---

## If you fall behind (recommended cuts, in order)

1. **LaTeX:** Keep a **single one-pager** template; drop extra LaTeX features beyond Module 3 checkpoint.  
2. **HCI breadth:** Require **one** strong interview **or** pair survey + mini heuristic; do not require all three at equal depth.  
3. **Pre-Next static work:** M4 focuses on the **login page**; M5 adds **grid + flex sections** to the broader project UI—avoid scope creep into a full multi-page static site before **Next.js**.  
4. **Next.js depth:** Restrict to an agreed subset (e.g. fixed routing pattern, one data-fetch pattern).  
5. **Database:** Start FastAPI week with **in-memory** store, swap to Postgres only after routes pass smoke tests (matches Module 8 → 9 split).

---

## After Semester 1 (Semester 2 preview)

Per calendar, **Semester 2** begins **2027-01-25**. If CS1 continues:

- Extend **Module 10** with deployment, auth stretch goals, or a second iteration of the book app.  
- Add pacing rows **Jan 25 → Jun 25** using the same PDF (Spring Festival, Qingming + spring break, Labor Day, Dragon Boat, last day of school).

Duplicate this file as `cs1-pacing-guide-s2.md` when you are ready to map those weeks.

---

## Alignment checklist (once per term)

- [ ] You have **confirmed** whether your section follows **CS on A** or **CS on B** (or a different cycle rule) and, if needed, **edited** the two numeric columns after long breaks to match the **registrar**.  
- [ ] Every **checkpoint** in [cs1-course-structure-overview.md](./cs1-course-structure-overview.md) fits the **sum of 90-minute CS blocks** for your column—not the count of Mon–Fri school days.  
- [ ] Major due dates avoid **full blackout** weeks and major **early-release** days where possible.  
- [ ] **Wednesday PD** weeks do not introduce the hardest new topic **and** a large homework due the next day.  
- [ ] **Book project** has at least one **integration buffer** before finals (here: **week 22**; consider stealing part of **week 21** if your sections have fewer CS blocks per week).
