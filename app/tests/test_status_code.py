from app.status_code import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_item():
    response = client.post("/items/?name=Amauri")
    assert response.status_code == 201


def test_create_item_params():
    params = {"name": "Amauri"}
    response = client.post("/items/", params=params)
    assert response.status_code == 201
