from datetime import datetime

from app.jsonable import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_update_item_status_code():
    data = {
        "title": "Título do Item",
        "timestamp": datetime.now().isoformat(),
        "description": "Descrição do Item"
    }
    response = client.post("/items/abc", json=data)
    assert response.status_code == 200


def test_update_item_2_status_code():
    data = {
        "title": "Título do Item",
        "timestamp": "2023-02-02T00:48",
        "description": "Descrição do Item"
    }
    response = client.post("/items/abc", json=data)
    assert response.status_code == 200


def test_update_item_bad_datetime_status_code():
    data = {
        "title": "Título do Item",
        "timestamp": "25/01/2023",
        "description": "Descrição do Item"
    }
    response = client.post("/items/abc", json=data)
    assert response.status_code == 422


def test_update_item_bad_datetime_2_status_code():
    data = {
        "title": "Título do Item",
        "timestamp": "2023-01-25",
        "description": "Descrição do Item"
    }
    response = client.post("/items/abc", json=data)
    assert response.status_code == 422


def test_update_item_bad_datetime_2_json():
    data = {
        "title": "Título do Item",
        "timestamp": "2023-01-25",
        "description": "Descrição do Item"
    }
    response = client.post("/items/abc", json=data)
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "timestamp"
                ],
                "msg": "invalid datetime format",
                "type": "value_error.datetime"
            }
        ]
    }


def test_read_product_status_code():
    response = client.get("/products/bar")
    assert response.status_code == 200


def test_read_product_json():
    response = client.get("/products/bar")
    assert response.json() == {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2,
        "tags": []
    }


def test_update_product_status_code():
    data = {
        "name": "Barz",
        "price": 3,
        "description": None,
    }
    response = client.put("/products/baz", json=data)
    assert response.status_code == 200


def test_update_product_json():
    data = {
        "name": "Barz",
        "price": 3,
        "description": None,
    }
    response = client.put("/products/bazx", json=data)
    assert response.json() == {
        "name": "Barz",
        "description": None,
        "price": 3,
        "tax": 10.5,
        "tags": []
    }
