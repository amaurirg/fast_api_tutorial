from fastapi.testclient import TestClient
from app.patch_update import app

client = TestClient(app)


def test_read_item_status_code():
    response = client.get("/items/bar")
    assert response.status_code == 200


def test_read_item_empty_data_json():
    data = {}
    response = client.patch("/items/bar", json=data)
    assert response.json() == {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2,
        "tags": []
    }

    
def test_read_item_json():
    data = {
        "name": "Bar",
        "price": 75.0,
        "tax": 23.8
    }
    response = client.patch("/items/bar", json=data)
    assert response.json() == {
        "name": "Bar",
        "description": "The bartenders",
        "price": 75.0,
        "tax": 23.8,
        "tags": []
    }



