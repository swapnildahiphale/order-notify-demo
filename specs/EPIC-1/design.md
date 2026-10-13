# EPIC-1 Design: Notify customers when an order ships

Status: draft

## Services touched
- **orders**: ship action, status endpoint, publishes `order.shipped`.
- **notifications**: subscribes to `order.shipped`, sends plain-text email via existing `send_email`.
- **shared `events.py`** (repo root, ~15 lines, added in STORY-1; deliberate small deviation from the one-pager's "no other services change", importable via `pythonpath = .`): in-process pub/sub. `subscribe(name, handler)`, `publish(name, payload)`, `reset()`. Handlers run synchronously in subscription order.

## Contracts
**Event `order.shipped`** payload: `{"order_id": str, "customer_email": str, "shipped_at": ISO-8601 UTC str}`.

**Endpoints** (via `orders.api.handle`):
- `POST /orders/:id/ship` -> 200 order (status `shipped`, `shipped_at` set) and publishes the event; 404 unknown order; 409 already shipped (no second event).
- `GET /orders/:id/status` -> 200 `{"id", "status": "placed"|"shipped", "shipped_at": str|null}`; 404 unknown order.
- Existing order dicts gain `status` (`placed` on create) and `shipped_at` (`None`).

**Notifications**: `notifications/consumer.py` has `register()` which subscribes `on_order_shipped`. It calls `send_email(customer_email, "Your order <order_id> has shipped", <plain-text body>)`. `register()` is idempotent (no double subscription). No app entry point exists, so `register()` is called only from tests for now; production wiring is a non-goal until an entry point exists.

## Data
In-memory only. `store.mark_shipped(order_id)` sets status and timestamp atomically and returns the order, raising `NotFound` / `AlreadyShipped` (defined in `orders/store.py`) that `api.handle` maps to 404 / 409. `shipped_at` is stored as the ISO string; the event payload is built from the store result, not the request. New `status`/`shipped_at` fields also appear in the `POST /orders` 201 body; existing tests are unaffected. New routes use fullmatch regexes, so `/ship` and `/status` do not collide with `/orders/:id`.

## Failure and edge cases
- Handler exception: `publish` catches each handler exception and logs it at error level, so the ship call still succeeds and the order stays `shipped`. Email loss is accepted for this demo (see non-goals).
- Double ship: 409, no duplicate email.
- Event published after the store update succeeds, never before.
- Malformed payload in consumer: raise; caught by `publish`; no email.

## Test strategy
- orders: ship 200/404/409; status for placed/shipped/unknown; event published exactly once with the exact payload (subscribe a spy); no event on 404/409.
- notifications: publishing `order.shipped` puts one email in `outbox` with the right recipient and subject; `register()` twice still sends one email.
- events: handler error does not stop other handlers or the publisher and is logged at error level; publish with no subscribers is a no-op.
- orders tests add an `events.reset()` fixture.
- Each service's tests use `events.reset()` / `email.clear()` fixtures. No cross-service end-to-end test beyond the notifications publish-driven test.

## Rejected
- Direct call from orders to notifications: couples services, not an event.
- Polling shared queue: needs a consumer loop, no value here.
- `PATCH /orders/:id`: needs transition validation we don't need.
- Payload with `order_id` only: forces notifications to call back into orders.

## Non-goals
Durable delivery, retries, or outbox pattern; real email provider; SMS/push; tracking numbers; templates; preferences/unsubscribe; auth on the ship endpoint. The 1-minute SLA is trivially met in-process; a real broker is a later epic.
