from fastapi.testclient import TestClient
from app.form import app

client = TestClient(app)


# def test_read_items_status_code():
#     response = client.get("/exceptions/items/abc")
#     assert response.status_code == 404
#
#
# def test_read_items_json():
#     response = client.get("/exceptions/items/abc")
#     assert response.json() == {"detail": "Item not found"}
