# order-notify-demo

A toy two-service repo used to demo an agent-driven workflow: product spec -> design -> stories -> code.

- `orders/` - in-memory order store and a small router (create order, get order).
- `notifications/` - stub `send_email` that appends to an in-memory outbox.
- `specs/EPIC-1/one-pager.md` - the product one-pager the workflow starts from.
- `.claude/` - the agent package (architect, design-reviewer, developer, and the `sdlc-design` / `sdlc-feature` skills).

Python 3 stdlib only, plus pytest.

## Run tests

    python -m venv .venv && . .venv/bin/activate && pip install pytest
    python -m pytest
