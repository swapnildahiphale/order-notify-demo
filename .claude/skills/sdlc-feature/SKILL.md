---
name: sdlc-feature
description: Implement one story from an epic's stories.md, test first, with plan and diff approval gates, and commit locally. Use when asked to implement a story (e.g. "implement STORY-1 of EPIC-1"). Never pushes.
---

# sdlc-feature

Input: an epic id and a story id, e.g. `EPIC-1 STORY-1`. Output: one local commit. Never push.

## Steps
1. **Read.** Read `specs/<EPIC>/design.md`, the story in `specs/<EPIC>/stories.md` (and any story it depends on), and the code you will touch.
2. **Plan.** Write a short plan (files, tests, acceptance criteria mapped to tests). Then call AskUserQuestion with the question "Approve plan?" and options `Approve` / `Request changes`. Do nothing else until answered; on `Request changes`, revise and ask again.
3. **Implement.** Tests first, then the minimum code, only in the story's owner service. Run `python -m pytest` until green. If pytest is missing (the shared venv is read-only), run once `python -m venv --system-site-packages ~/.pytest-venv && ~/.pytest-venv/bin/pip install -q pytest`, then use `~/.pytest-venv/bin/python -m pytest` instead. Never add it to the repo.
4. **Diff.** Show `git diff --stat` and the key hunks. Then call AskUserQuestion with the question "Approve diff?" and options `Approve` / `Request changes`. On `Request changes`, revise, re-run pytest, ask again.
5. **Commit.** On `Approve`, `git add` and commit locally, no prompts, with `git -c user.name=developer -c user.email=developer@example.com commit -m "<STORY-ID>: <summary>"`. Never push. Do not ask about the commit identity. Reply with the commit hash and the pytest summary line, then stop.

## Design gaps
If the design does not cover something you must decide (payload field, status code, failure behavior, ownership), stop at once and output exactly one line, then wait:

`DESIGN QUESTION: <question>`

Do not guess and do not edit the design. A human relays the answer; then continue.
