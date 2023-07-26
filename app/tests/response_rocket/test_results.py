from fastapi.testclient import TestClient
from app.tests.response_rocket.response_rocket import app

client = TestClient(app)


# SIMPLE RESULTS FIELDS
def test_results_empty_fields():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "carrier": {},
                "origin": "",
                "destination": "",
                "date_outbound": "",
                "date_inbound": None,
                "adults": 0,
                "children": 0,
                "infants": 0,
                "direction": "",
                "promocode": None
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }
    response = client.post("/result/", json=data)
    # assert response.status_code == 200
    assert response.json() == data
    # "carrier": {
    #     "id": None,
    #     "name": None,
    #     "iata_code": None
    # },


def test_results_no_str_fields():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "carrier": {},
                "date_inbound": None,
                "adults": 0,
                "children": 0,
                "infants": 0,
                "promocode": None
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "carrier": {},
                "origin": None,
                "destination": None,
                "date_outbound": None,
                "date_inbound": None,
                "adults": 0,
                "children": 0,
                "infants": 0,
                "direction": None,
                "promocode": None
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }


def test_results_no_none_fields():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "carrier": {},
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "carrier": {},
                "origin": None,
                "destination": None,
                "date_outbound": None,
                "date_inbound": None,
                "adults": 0,
                "children": 0,
                "infants": 0,
                "direction": None,
                "promocode": None
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }


def test_result_empty_flights_and_carrier():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "carrier": {},
                "origin": "CGH",
                "destination": "MAO",
                "date_outbound": "2023-08-16T00:00:00-03:00",
                "date_inbound": None,
                "adults": 1,
                "children": 0,
                "infants": 0,
                "direction": "outbound",
                "promocode": None
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_result_no_carrier():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "origin": "CGH",
                "destination": "MAO",
                "date_outbound": "2023-08-16T00:00:00-03:00",
                "date_inbound": None,
                "adults": 1,
                "children": 0,
                "infants": 0,
                "direction": "outbound",
                "promocode": None
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "carrier": {},
                "origin": "CGH",
                "destination": "MAO",
                "date_outbound": "2023-08-16T00:00:00-03:00",
                "date_inbound": None,
                "adults": 1,
                "children": 0,
                "infants": 0,
                "direction": "outbound",
                "promocode": None
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }


def test_result_carrier():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "carrier": {
                    "id": 317,
                    "name": "GOL LINHAS AEREAS S.A.",
                    "iata_code": "G3"
                },
                "origin": "CGH",
                "destination": "MAO",
                "date_outbound": "2023-08-16T00:00:00-03:00",
                "date_inbound": None,
                "adults": 1,
                "children": 0,
                "infants": 0,
                "direction": "outbound",
                "promocode": None
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_result_bad_carrier():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [],
                "carrier": {
                    "id": "A",
                    "name": 3,
                    "iata_code": ["G3"]
                },
                "origin": "CGH",
                "destination": "MAO",
                "date_outbound": "2023-08-16T00:00:00-03:00",
                "date_inbound": None,
                "adults": 1,
                "children": 0,
                "infants": 0,
                "direction": "outbound",
                "promocode": None
            }
        ],
        "min_price": 1554.52,
        "max_price": 2298.12
    }
    response = client.post("/result/", json=data)
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {'loc': ['body', 'results', 0, 'carrier', 'id'],
             'msg': 'value is not a valid integer',
             'type': 'type_error.integer'},
            {'loc': ['body', 'results', 0, 'carrier', 'iata_code'],
             'msg': 'str type expected',
             'type': 'type_error.str'}
        ]
    }
