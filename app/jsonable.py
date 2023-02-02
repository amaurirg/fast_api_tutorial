from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()
fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


class Product(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


@app.post("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data

    # Comparação entre item e json_compatible_item_data
    # item = Item(
    #     title='Título do Item',
    #     timestamp=datetime.datetime(2023, 2, 1, 22, 59, 31, 529459),
    #     description='Descrição do Item'
    # )
    # json_compatible_item_data = {
    #     'title': 'Título do Item',
    #     'timestamp': '2023-02-01T22:59:31.529459',
    #     'description': 'Descrição do Item'
    # }

    return fake_db


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: str):
    return items[product_id]


@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: str, item: Product):
    update_item_encoded = jsonable_encoder(item)
    items[product_id] = update_item_encoded
    return update_item_encoded
