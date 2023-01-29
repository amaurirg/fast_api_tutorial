from typing import Optional

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


class Image(BaseModel):
    # url: str
    url: HttpUrl
    name: str


class Product(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        description="The description of the item",
        max_length=30
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than zero"
    )
    tax: float | None = None
    key_words: list[str] = list()
    image: Optional[list[Image] | None]


@app.get("/")
async def hello_world():
    return {"Hello": "World"}


@app.get("/items/")
async def read_items(date_now: str, q: str | None = Query(
    default=None, min_length=3, max_length=5, regex="^teste$")):
    results = {"date_now": date_now, "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update(q=q)
    return results


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update(price_with_tax=price_with_tax)
    return item_dict


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=5, le=10),
        q: str | None = None,
        item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.get("/new-items/")
async def read_new_items(q: list[str] | None = Query(
    default=None,
    alias="item-query",
    title="Query string",
    description="Query string for the items to search in the database that have a good match",
    deprecated=True,
)
):
    query_items = {"q": q}
    return query_items


@app.put("/new-items/{item_id}")
async def update_new_items(item_id: int, item: Item, user: User, importance: int = Body(..., gt=0)):
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance
    }
    return results


@app.post("/new-items/")
async def create_new_item(item: Item = Body(..., embed=True)):
    result = {"item_id": 1, "item": item}
    return result


@app.get("/products/")
async def read_products():
    results = {
        "products": [
            {
                "name": "Carro",
                "description": "Descrição do carro",
                "price": 15000,
                "tax": 1500
            }
        ]
    }
    return results


@app.post("/products/create/")
async def create_product(
        product: Product = Body(
            ...,
            example={
                "name": "Carro",
                "description": "Descrição do carro",
                "price": 15000,
                "tax": 1500
            }
        )):
    results = {
        "products": [
            {
                "name": "Carro",
                "description": "Descrição do carro",
                "price": 15000,
                "tax": 1500
            }
        ]
    }
    results["products"].append(product.dict())
    return results
