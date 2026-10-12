---
name: sdlc-design
description: Turn an epic's product one-pager into an approved design.md and stories.md. Use when asked to design an epic (e.g. "design EPIC-1"). Writes specs only, never code.
---

# sdlc-design

Input: an epic id, e.g. `EPIC-1`. Output: `specs/<EPIC>/design.md` and `specs/<EPIC>/stories.md`. Never write or edit code.

## Steps
1. **Read.** Read `specs/<EPIC>/one-pager.md` and the code of every service it touches (`orders/`, `notifications/`, ...).
2. **Draft design.** Write `specs/<EPIC>/design.md` with the user: services touched, contracts (events, endpoints, payloads), data, failure and edge cases, test strategy, non-goals. Keep it to about one page. Use AskUserQuestion for each genuinely open decision, with 2-3 options and a recommendation.
3. **Review.** Run the `design-reviewer` subagent on the epic (fresh context). Fix every blocking finding in `design.md`; apply suggestions only if they keep the design small. Re-run the reviewer if you changed contracts.
4. **Approve architecture.** AskUserQuestion: "Approve architecture?" with options `Approve` / `Request changes`. On `Request changes`, collect the changes, edit `design.md`, return to step 3.
5. **Write stories.** On approval write `specs/<EPIC>/stories.md`. For each story: `id` (STORY-1, ...), title, owner service, acceptance criteria, test impact, dependencies. Order so dependencies point backwards (e.g. consumer depends on producer).
6. **Approve stories.** AskUserQuestion: "Approve stories?" with `Approve` / `Request changes`. Loop on changes.
7. **Done.** Summarize in two lines: design and story files written. Stop. Do not start implementation.
