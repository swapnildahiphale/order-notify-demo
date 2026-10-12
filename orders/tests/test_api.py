import pytest

from orders import api, store


@pytest.fixture(autouse=True)
def clean():
    store.reset()


def test_create_and_get_order():
    status, order = api.handle("POST", "/orders", {"customer_email": "a@example.com", "items": ["book"]})
    assert status == 201
    status, fetched = api.handle("GET", f"/orders/{order['id']}")
    assert status == 200
    assert fetched["customer_email"] == "a@example.com"


def test_create_requires_fields():
    status, _ = api.handle("POST", "/orders", {"items": []})
    assert status == 400


def test_get_unknown_order_is_404():
    status, _ = api.handle("GET", "/orders/nope")
    assert status == 404
