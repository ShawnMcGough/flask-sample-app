# tests/test_app.py

import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_hello_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello, Flask!"


def test_add_item_route(client):
    response = client.post('/items', json={"name": "item1"})
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Item added successfully'}


def test_get_item_route(client):
    client.post('/items', json={"name": "item1"})
    response = client.get('/items/0')
    assert response.status_code == 200
    assert response.get_json() == {'item': {'name': 'item1'}}


def test_get_nonexistent_item_route(client):
    response = client.get('/items/99999999')
    assert response.status_code == 404
    assert response.get_json() == {'error': 'Item not found'}

