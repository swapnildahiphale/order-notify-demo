# EPIC-1 Stories

## STORY-1: Emit `order.shipped` and expose order status
- **Owner:** orders
- **Acceptance criteria:**
  - New root `events.py` with `subscribe`, `publish`, `reset`; a handler exception is logged at error level and does not stop other handlers or the publisher; publish with no subscribers is a no-op.
  - Orders get `status` (`placed`) and `shipped_at` (`None`) on create.
  - `POST /orders/:id/ship` returns 200 with status `shipped` and `shipped_at` set; 404 for an unknown order; 409 if already shipped.
  - On a successful ship, exactly one `order.shipped` event is published with `{order_id, customer_email, shipped_at}`, built from the store result and published after the store update. No event on 404/409.
  - `GET /orders/:id/status` returns 200 `{id, status, shipped_at}`; 404 for an unknown order.
- **Test impact:** New tests for events, ship (200/404/409), status, and event payload (spy subscriber). Add an `events.reset()` fixture to orders tests. Existing tests are unchanged and still pass.
- **Dependencies:** none.

## STORY-2: Send a stub email on `order.shipped`
- **Owner:** notifications
- **Acceptance criteria:**
  - `notifications/consumer.py` provides `on_order_shipped` and an idempotent `register()` that subscribes it to `order.shipped`.
  - A published `order.shipped` event puts exactly one email in `outbox`, addressed to `customer_email`, with subject "Your order <order_id> has shipped" and a plain-text body.
  - Calling `register()` twice still sends one email per event.
  - A malformed payload sends no email, and the exception is contained by `publish`.
- **Test impact:** New consumer tests, using `events.reset()` and `email.clear()` fixtures. Existing `test_email.py` is unchanged.
- **Dependencies:** STORY-1.
