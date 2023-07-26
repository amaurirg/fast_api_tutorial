from typing import Optional, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, EmailStr, Field

from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)


class Address(BaseModel):
    street: str = Field(alias='rua')
    number: int = Field(alias='número')


class UserBase(BaseModel):
    username: str = Field(alias='nome')
    address: Address = Field(alias='endereco', default={})


@app.post("/new-user/")
async def create_new_user(user: UserBase):
    result = user.dict()
    return result


def test_create_new_user():
    data = {
        "nome": "user_teste",
        "endereco": {
            "rua": "Rua teste",
            "número": 123
        }
    }
    response = client.post("/new-user/", json=data)
    assert response.json() == {
        "username": "user_teste",
        "address": {
            "street": "Rua teste",
            "number": 123
        }
    }
