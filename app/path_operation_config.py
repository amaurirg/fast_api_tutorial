from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


class Tags(Enum):
    items = "items"
    users = "users"

# @app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["items"])
# usando Enum
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=[Tags.items])
async def create_item(item: Item):
    return item


@app.get("/items/", tags=[Tags.items])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=[Tags.users])
async def read_users():
    return [{"username": "johndoe"}]
