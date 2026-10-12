"""In-memory order store."""
import itertools

_ids = itertools.count(1)
_orders = {}


def create_order(customer_email, items):
    order_id = f"ord-{next(_ids)}"
    order = {"id": order_id, "customer_email": customer_email, "items": list(items)}
    _orders[order_id] = order
    return dict(order)


def get_order(order_id):
    order = _orders.get(order_id)
    return dict(order) if order else None


def reset():
    _orders.clear()
