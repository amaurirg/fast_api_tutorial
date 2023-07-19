from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Results(BaseModel):
    flights: list
    carrier: list
    origin: str
    destination: str
    date_outbound: str
    date_inbound: str
    adults: int
    children: int
    infants: int
    direction: str
    promocode: str = None


class Response(BaseModel):
    count: int = None
    next: bool = None
    previous: bool = None
    results: list = []
    min_price: float = None
    max_price: float = None


@app.post("/result/")
async def get_result(response: Response):
    return response
