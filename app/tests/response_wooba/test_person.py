from typing import Union

from fastapi.testclient import TestClient
from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.tests.response_wooba.trecho_wooba import trechos

app = FastAPI()
client = TestClient(app)


class Carrier(BaseModel):
    id: int = Field(default=None, alias="Id")
    name: str = Field(default=None, alias="Descricao")
    iata_code: str = Field(default=None, alias="CodigoIata")


class Results(BaseModel):
    # flights: Union[list, Flights] = []
    flights: list = Field(default=[], alias="Voos")
    # carrier: Union[dict, Carrier] = {}
    # carrier: Carrier = {}  # Resposta: 'carrier': {'iata_code': None, 'id': None, 'name': None}
    carrier: dict = Field(default={}, alias="CiaMandatoria")
    origin: str = None
    destination: str = None
    date_outbound: str = None
    date_inbound: str = None
    adults: int = 0
    children: int = 0
    infants: int = 0
    direction: str = None
    promocode: str = None


class ResponseAPI(BaseModel):
    count: int = 0
    next: bool = None
    previous: bool = None
    results: list[Results] = Field(default=[], alias="ViagensTrecho1")
    min_price: float = 0
    max_price: float = 0


@app.post("/", response_model=ResponseAPI)
# @app.post("/")
# async def handle(request: dict):
# return request
async def handle(response: ResponseAPI):
    return response
    results = request.get("ViagensTrecho1")
    response = {
        "count": 0,
        # "next": ,
        # "previous": ,
        # "results": Results(request.get("ViagensTrecho1")),
        "results": results,
        # "min_price": ,
        # "max_price": ,
    }
    return response


def test_handle_empty_data():
    data = {}
    response = client.post("/", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_handle():
    # data = {
    #     "teste": "TESTE"
    # }
    response = client.post("/", json=trechos)
    assert response.status_code == 200
    assert response.json() == {}


def test_bad_handle():
    data = [1, 2, 3]
    response = client.post("/", json=data)
    assert response.status_code == 422
    assert response.json() == {
        'detail': [{
            'loc': ['body'],
            'msg': 'value is not a valid dict',
            'type': 'type_error.dict'
        }]
    }


