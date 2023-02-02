from fastapi.testclient import TestClient
from app.path_operation_config import app

client = TestClient(app)


# Form
def test_create_item_status_code():
    data = {
        "name": "Product 1",
        "description": "Description of the Product 1",
        "price": 120.5,
        "tax": 13.7,
        "tags": ["TV", "Smart"],
    }
    response = client.post("/items/", json=data)
    assert response.status_code == 201


def test_create_item_json():
    data = {
        "name": "Product 1",
        "description": "Description of the Product 1",
        "price": 120.5,
        "tax": 13.7,
        "tags": ["TV", "Smart", "TV"]
    }
    response = client.post("/items/", json=data)
    assert response.json() == {
        "name": "Product 1",
        "description": "Description of the Product 1",
        "price": 120.5,
        "tax": 13.7,
        "tags": ["Smart", "TV"]
    } or {
        "name": "Product 1",
        "description": "Description of the Product 1",
        "price": 120.5,
        "tax": 13.7,
        "tags": ["TV", "Smart"]
    }


def test_get_items_status_code():
    response = client.get("/items/")
    assert response.status_code == 200


def test_get_items_json():
    response = client.get("/items/")
    assert response.json() == [{"name": "Foo", "price": 42}]


def test_get_users_status_code():
    response = client.get("/users/")
    assert response.status_code == 200


def test_get_users_json():
    response = client.get("/users/")
    assert response.json() == [{"username": "johndoe"}]
