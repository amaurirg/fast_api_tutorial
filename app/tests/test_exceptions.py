from fastapi.testclient import TestClient
from app.exceptions import app

client = TestClient(app)


def test_read_items_status_code():
    response = client.get("/exceptions/items/abc")
    assert response.status_code == 404


def test_read_items_json():
    response = client.get("/exceptions/items/foo")
    assert response.json() == {"item": "The Foo Wrestlers"}


def test_bad_read_items_json():
    response = client.get("/exceptions/items/abc")
    assert response.json() == {"detail": "Item not found"}

