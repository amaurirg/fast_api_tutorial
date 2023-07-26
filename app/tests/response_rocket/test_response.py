from fastapi.testclient import TestClient
from app.tests.response_rocket.response_rocket import app

client = TestClient(app)


def test_response_without_data():
    data = {}
    response = client.post("/result/", json=data)
    # assert response.status_code == 200
    assert response.json() == {
        "count": 0,
        "next": None,
        "previous": None,
        "results": [],
        "min_price": 0,
        "max_price": 0
    }


def test_response_bad_integers_fields():
    data = {
        "count": "A",
        "min_price": "A",
        "max_price": "A"
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {'loc': ['body', 'count'],
             'msg': 'value is not a valid integer',
             'type': 'type_error.integer'},
            {'loc': ['body', 'min_price'],
             'msg': 'value is not a valid float',
             'type': 'type_error.float'},
            {'loc': ['body', 'max_price'],
             'msg': 'value is not a valid float',
             'type': 'type_error.float'}
        ]
    }


def test_response_bad_bool_fields():
    data = {
        "count": 0,
        "next": 3,
        "previous": 3,
        "min_price": 0,
        "max_price": 0
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {'loc': ['body', 'next'],
             'msg': 'value could not be parsed to a boolean',
             'type': 'type_error.bool'},
            {'loc': ['body', 'previous'],
             'msg': 'value could not be parsed to a boolean',
             'type': 'type_error.bool'}
        ]
    }


def test_response_without_results():
    data = {
        "count": 0,
        "next": None,
        "previous": None,
        "min_price": 0,
        "max_price": 0
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "count": 0,
        "next": None,
        "previous": None,
        "results": [],
        "min_price": 0,
        "max_price": 0
    }


def test_response_empty_results():
    data = {
        "count": 0,
        "next": None,
        "previous": None,
        "results": [],
        "min_price": 0,
        "max_price": 0
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 200
    assert response.json() == data
