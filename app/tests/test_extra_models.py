from app.extra_models import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_user_status_code():
    data = {
        "username": "amaurirg",
        "password": "1234",
        "email": "amauri@gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }
    response = client.post("/user/", json=data)
    assert response.status_code == 200


def test_create_user_json():
    data = {
        "username": "amaurirg",
        "password": "1234",
        "email": "amauri@gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }
    response = client.post("/user/", json=data)
    assert response.json() == {
        "username": "amaurirg",
        "email": "amauri@gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }


# GET
# url = "/items/{item_id}"
def test_read_item_status_code():
    response = client.get("/items/item1")
    assert response.status_code == 200


def test_read_item_json():
    response = client.get("/items/item1")
    assert response.json() == {
        "description": "All my friends drive a low rider",
        "type": "car"
    }


def test_read_items_status_code():
    response = client.get("/items/")
    assert response.status_code == 200


def test_read_items_json():
    response = client.get("/items/")
    assert response.json() == [
        {"name": "Foo", "description": "There comes my hero"},
        {"name": "Red", "description": "It's my aeroplane"},
    ]


# GET
# url = "/keyword-weights/"
def test_read_keyword_weights_status_code():
    response = client.get("/keyword-weights/")
    assert response.status_code == 200


def test_read_keyword_weights_json():
    response = client.get("/keyword-weights/")
    assert response.json() == {"foo": 2.3, "bar": 3.4}
