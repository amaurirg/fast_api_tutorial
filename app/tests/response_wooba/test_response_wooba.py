from fastapi.testclient import TestClient
from app.tests.response_rocket.response_rocket import app
from app.tests.response_wooba.trecho_wooba import trechos


client = TestClient(app)


def test_response_without_results():
    # data = {
    #     "count": 0,
    #     "next": None,
    #     "previous": None,
    #     "min_price": 0,
    #     "max_price": 0
    # }
    response = client.post("/result/", json=trechos)
    assert response.status_code == 200