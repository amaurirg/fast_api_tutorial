from fastapi.testclient import TestClient
from app.tests.response_rocket.response_rocket import app

client = TestClient(app)


# TEST FLIGHTS
def test_flights_simple_items_json():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [
                    {
                        "id": 521795,
                        "origin": {},
                        "destination": {},
                        "links": [],
                        "segments": [],
                        "prices": [],
                        "direction": "outbound",
                        "travel_time": "345",
                        "direct": False
                    }
                ],
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
    assert response.json() == data


def test_flights_links():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [
                    {
                        "id": 521795,
                        "origin": {},
                        "destination": {},
                        "links": [
                            {
                                "pricing": "/pricing?hash=81a7666c6967687473d9e05b7b226d6f64656c223a2022666c69676874732e666c69676874222c2022706b223a203532313739352c20226669656c6473223a207b226a6f75726e6579223a203133303830382c20226f726967696e223a2034333939302c202264657374696e6174696f6e223a2034343039352c2022646972656374696f6e223a20226f7574626f756e64222c202274726176656c5f74696d65223a2022333435222c202265787465726e616c5f6964223a202230222c2022646972656374223a2066616c73652c202270726f76696465725f726573706f6e7365223a206e756c6c7d7d5d"
                            }
                        ],
                        "segments": [],
                        "prices": [],
                        "direction": "outbound",
                        "travel_time": "345",
                        "direct": False
                    }
                ],
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
    assert response.json() == data


def test_flights_origin():
    data = {
        "count": 19,
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [
                    {
                        "id": 521795,
                        "origin": {
                            "state": {
                                "country": {
                                    "name": "Brasil",
                                    "code": "BR"
                                },
                                "name": "São Paulo",
                                "initials": "SP"
                            },
                            "name": "São Paulo"
                        },
                        "destination": {},
                        "links": [
                            {
                                "pricing": "/pricing?hash=81a7666c6967687473d9e05b7b226d6f64656c223a2022666c69676874732e666c69676874222c2022706b223a203532313739352c20226669656c6473223a207b226a6f75726e6579223a203133303830382c20226f726967696e223a2034333939302c202264657374696e6174696f6e223a2034343039352c2022646972656374696f6e223a20226f7574626f756e64222c202274726176656c5f74696d65223a2022333435222c202265787465726e616c5f6964223a202230222c2022646972656374223a2066616c73652c202270726f76696465725f726573706f6e7365223a206e756c6c7d7d5d"
                            }
                        ],
                        "segments": [],
                        "prices": [],
                        "direction": "outbound",
                        "travel_time": "345",
                        "direct": False
                    }
                ],
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
    assert response.json() == data
