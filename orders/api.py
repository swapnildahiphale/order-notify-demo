"""Plain function router: (method, path, body) -> (status, json-able)."""
import re

from orders import store


def handle(method, path, body=None):
    if method == "POST" and path == "/orders":
        body = body or {}
        if not body.get("customer_email") or not body.get("items"):
            return 400, {"error": "customer_email and items are required"}
        return 201, store.create_order(body["customer_email"], body["items"])
    m = re.fullmatch(r"/orders/([\w-]+)", path)
    if method == "GET" and m:
        order = store.get_order(m.group(1))
        return (200, order) if order else (404, {"error": "not found"})
    return 404, {"error": "no such route"}
