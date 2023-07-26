from typing import Optional, Union, Dict

from fastapi import Body, FastAPI
from pydantic import BaseModel, EmailStr, Field, validator

from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)


class Carrier(BaseModel):
    id: int
    name: str
    iata_code: str

    # @validator("*", pre=True)
    # def validate_fields(cls, values):
    #     if not values:
    #         return None
    #     return values


class Results(BaseModel):
    # carrier: Union[None, Carrier] = Field(default=None)
    # carrier: Carrier = {}
    carrier: Union[Carrier, dict] = None

    @validator("carrier")
    def check_carrier_none(cls, value):
        if not value:
            return {}
        return value


class Response(BaseModel):
    count: int = 0
    # results: Union[list, Results] = Field(default=[])
    results: Results = []


# @app.post("/response/", response_model=Response, response_model_exclude_defaults=True)
@app.post("/response/", response_model=Response, response_model_exclude_none=True)
# @app.post("/response/", response_model=Results)
# @app.post("/result/")
async def get_response(response: Response):
    return response


# @app.post("/result/", response_model=Results, response_model_exclude_defaults=True)
@app.post("/result/", response_model=Results)
# @app.post("/result/")
async def get_result(response: Results):
    return response


# @app.post("/carrier/", response_model=Carrier, response_model_exclude_defaults=True)
# @app.post("/carrier/", response_model=Carrier)
@app.post("/carrier/")
async def get_carrier(carrier: dict):
    return carrier


def test_carrier():
    data = {}
    response = client.post("/carrier/", json=data)
    assert response.json() == {}


def test_bad_carrier():
    data = {
        "id": "A",
        "name": [1, 2, 3],
        "iata_code": ["A"]
    }
    response = client.post("/carrier/", json=data)
    assert response.json() == {
        'detail': [
            {'loc': ['body', 'id'],
             'msg': 'value is not a valid integer',
             'type': 'type_error.integer'},
            {'loc': ['body', 'name'],
             'msg': 'str type expected',
             'type': 'type_error.str'},
            {'loc': ['body', 'iata_code'],
             'msg': 'str type expected',
             'type': 'type_error.str'}
                   ]
    }


def test_results():
    data = {
        "carrier": {}
    }
    response = client.post("/result/", json=data)
    assert response.json() == {'carrier': {}}


def test_bad_results():
    data = {
        "carrier": {
            "id": "A",
            "name": [1, 2, 3],
            "iata_code": 3
        }
    }
    response = client.post("/result/", json=data)
    assert response.json() == {
        'detail': [
            {'loc': ['body', 'carrier', 'id'],
             'msg': 'value is not a valid integer',
             'type': 'type_error.integer'},
            {'loc': ['body', 'carrier', 'name'],
             'msg': 'str type expected',
             'type': 'type_error.str'}
        ]
    }


def test_response():
    data = {}
    response = client.post("/response/", json=data)
    assert response.json() == {
        "count": 0,
        "results": []
    }


def test_response_results():
    data = {
        "count": 0,
        "results": [
            {
                "carrier": {}
            }
        ]
    }
    response = client.post("/response/", json=data)
    assert response.json() == {
        "count": 0,
        "results": []
    }