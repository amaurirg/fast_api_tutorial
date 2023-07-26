from typing import Union, Optional, Dict

from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, parse_obj_as, validator

app = FastAPI()


class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    country: Country
    name: str
    initials: str


class Origin(BaseModel):
    state: State
    name: str


class Destination(BaseModel):
    state: State
    name: str


class Flights(BaseModel):
    id: int = None
    origin: Origin = {}
    destination: Destination = {}
    links: Dict[str, str] = {}
    segments: list = []
    prices: list = []
    direction: str = None
    travel_time: str = None
    direct: bool = None


class Carrier(BaseModel):
    id: int = None
    name: str = None
    iata_code: str = None

    @validator("*", pre=True)
    def validate_fields(cls, values):
        if not values:
            return {}
        return values



class Results(BaseModel):
    # flights: Union[list, Flights] = []
    flights: list = Field(default=[], alias="Voos")
    # flights: list = []
    # carrier: Union[dict, Carrier] = {}
    carrier: Carrier = {}  # Resposta: 'carrier': {'iata_code': None, 'id': None, 'name': None}
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
    results: list[Results] = Field(default=[])
    min_price: float = 0
    max_price: float = 0


@app.post(
    "/result/",
    # response_model=ResponseAPI,
    # response_model_exclude_none=True,
    # response_model_include={"count", "results"}
)
# async def get_result(response: ResponseAPI):
async def get_result(response: dict):
    return response
    # results = response.results
    # if not all(results[0].carrier.dict().values()):
    #     results[0].carrier = {}
    # resposta = {
    #     "count": response.count,
    #     "results": results
    # }
    # return resposta

