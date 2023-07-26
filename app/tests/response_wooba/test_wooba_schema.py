from fastapi.testclient import TestClient

from app.tests.response_wooba.api_content import api_content
from app.tests.response_wooba.wooba_schema import app_wooba, ApiContent, CiaOrigemDestino, ViagensTrecho

client = TestClient(app_wooba)


def test_create_obj_ApiContent_without_trecho2():
    data = api_content
    api = ApiContent(**data)
    assert isinstance(api, ApiContent)
    assert isinstance(api.cia[0], CiaOrigemDestino)
    assert isinstance(api.destino, CiaOrigemDestino)
    assert isinstance(api.origem, CiaOrigemDestino)
    assert isinstance(api.viagens_trecho1[0], ViagensTrecho)
    assert isinstance(api.viagens_trecho2, list)


def test_response_empty_data():
    data = {}
    response = client.post("/results/", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_response_data_api_content_without_some_data():
    data = {
        'Data': '/Date(1690217747176-0300)/',
        'DataVersao': '24/07/2023',
        'SessaoExpirada': False
    }
    response = client.post("/results/", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_response_data_api_content_full():
    data = api_content
    response = client.post("/results/", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_response_data_api_content_without_Recomendacoes():
    data = api_content
    del data["Recomendacoes"]
    response = client.post("/results/", json=data)
    assert response.status_code == 200
    assert response.json() == data
