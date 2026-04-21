# Commit message guide (CS1)

Good commits help you, your teammates, and your teacher **review PRs** and **find bugs later**.

---

## Format (recommended)

```text
<type>: <short summary in imperative mood>

Optional body: what changed and why. Wrap at ~72 chars per line.
```

**Examples**

- `fix: validate dice count before roll`
- `feat: add books list page in Next`
- `docs: update README run instructions`
- `style: format login page with Prettier`

Common **types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.

---

## Rules

1. **One idea per commit** when possible—easier to revert and to review.  
2. **Summary line:** about **50 characters or less** is ideal; **hard cap ~72**.  
3. Use **imperative** mood: “add” not “added”, “fix” not “fixes”.  
4. **No vague messages:** avoid `update`, `changes`, `fix stuff`, `asdf`.  
5. If the change is **non-obvious**, add a **body** (blank line after summary, then details).

---

## PR discipline

- Prefer **small PRs** linked to a **clear purpose** (one feature or one bugfix).  
- In the PR description, say **what** changed and **how to test** it (2–4 bullets).  
- Use the repo **PR template** when opening a pull request.
