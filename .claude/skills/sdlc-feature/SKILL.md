---
name: sdlc-feature
description: Implement one story from an epic's stories.md, test first, with plan and diff approval gates, and commit locally. Use when asked to implement a story (e.g. "implement STORY-1 of EPIC-1"). Never pushes.
---

# sdlc-feature

Input: an epic id and a story id, e.g. `EPIC-1 STORY-1`. Output: one local commit. Never push.

## Steps
1. **Read.** Read `specs/<EPIC>/design.md`, the story in `specs/<EPIC>/stories.md` (and any story it depends on), and the code you will touch.
2. **Plan.** Write a short plan: files to change, tests to add, how acceptance criteria map to tests.
3. **Approve plan.** AskUserQuestion: "Approve plan?" with `Approve` / `Request changes`. Loop on changes.
4. **Implement.** Write the tests first and see them fail, then write the minimum code. Stay within the story's owner service.
5. **Verify.** Run `python -m pytest`. Fix until green.
6. **Show diff.** Show `git diff --stat` and the key part of the diff.
7. **Approve diff.** AskUserQuestion: "Approve diff?" with `Approve` / `Request changes`. Loop on changes.
8. **Commit.** On approve, `git add` and commit locally with a plain message that names the story. Do not push.

## Design gaps
If the design does not cover something you must decide (payload field, status code, ownership, failure behavior), stop immediately and output exactly one line:

`DESIGN QUESTION: <question>`

Do not guess and do not edit the design. A human relays the answer; then continue.
