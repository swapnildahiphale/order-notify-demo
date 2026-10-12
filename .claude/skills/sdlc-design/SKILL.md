---
name: sdlc-design
description: Turn an epic's product one-pager into an approved design.md and stories.md. Use when asked to design an epic (e.g. "design EPIC-1"). Writes specs only, never code.
---

# sdlc-design

Input: an epic id, e.g. `EPIC-1`. Output: `specs/<EPIC>/design.md` and `specs/<EPIC>/stories.md`. Never write or edit code.

## Steps
1. **Read.** Read `specs/<EPIC>/one-pager.md` and the code of every service it touches.
2. **Clarify.** Ask at most 2-3 questions in ONE AskUserQuestion call, only for decisions the one-pager and code leave open (e.g. event payload, idempotency). Put your recommended option first and mark it "(Recommended)". Never ask what is already answered.
3. **Draft.** Write `specs/<EPIC>/design.md`, about one page: services touched, contracts (event name and payload, endpoints and status codes), failure cases, test strategy, non-goals.
4. **Review.** Run the `design-reviewer` subagent with the Agent tool, `subagent_type: design-reviewer` and `run_in_background: false`. It must run in the FOREGROUND: wait for its result in the same turn, never end your turn while it runs. Fix every blocking finding in `design.md`; take suggestions only if they keep the design small.
5. **Approve architecture.** Call AskUserQuestion with the question "Approve architecture?" and options `Approve` / `Request changes`. Do nothing else until answered. On `Request changes`, apply the feedback, then repeat from step 4.
6. **Stories.** On `Approve`, write `specs/<EPIC>/stories.md` with exactly:
   - STORY-1 (owner: orders): emit `order.shipped` when an order ships, and `GET /orders/:id/status`.
   - STORY-2 (owner: notifications): consume `order.shipped` and send a stub email. Depends on STORY-1.
   Each story has: id, title, owner service, acceptance criteria, test impact, dependencies.
7. **Stop.** Reply with two lines naming the files written. Do not ask further questions and do not start implementation.
