"""import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_create_order_service(order):
    order = order.json
    pytest.assume(order.status.startswith('200'))
    pytest.assume(order['_id'])
    pytest.assume(order['client_name'])
    pytest.assume(order['client_dni'])
    pytest.assume(order['client_address'])
    pytest.assume(order['client_phone'])
    pytest.assume(order['date'])
    pytest.assume(order['total_price'])
    pytest.assume(order['size_id'])
    pytest.assume(order['size'])
    pytest.assume(order['order_detail'])


def test_get_order_by_id_service(client, order, order_uri):
    current_order = order.json
    response = client.get(f'{order_uri}id/{current_order["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_order = response.json
    for param, value in current_order.items():
        pytest.assume(returned_order[param] == value)


def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(order['_id'] in returned_orders)"""
