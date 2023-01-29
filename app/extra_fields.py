from datetime import datetime, timedelta, time, date
from uuid import UUID

from fastapi import FastAPI, Body, Cookie, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()


class DatetimeModel(BaseModel):
    birth_date: date
    current_time: time
    current_date: datetime


class UuidModel(BaseModel):
    id: UUID = None


@app.post("/items/datetime/")
async def items_datetime(item: DatetimeModel) -> DatetimeModel:
    # return {
    #     "birth_date": item.birth_date,
    #     "current_time": item.current_time,
    #     "current_date": item.current_date
    # }

    # Declarando o retorno da função (-> DatetimeModel:), basta retornar item
    return item


@app.post("/items/uuid/")
async def item_uuid(item: UuidModel) -> UuidModel:
    # return {"id": item.id}
    return item


@app.get("/items/cookies/")
async def item_cookies(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
}


@app.get("/items/list/")
async def read_items_list() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item) -> Any:
#     return item


@app.get("/item/{item_id}", response_model=Item, response_model_exclude_unset=True, response_model_exclude_none=True)
async def read_item(item_id: str) -> Item:
    return items[item_id]


@app.get("/item/{item_id}/name", response_model=Item, response_model_include={"name", "description"})
# Se você usar list ou tuple em vez de set , FastAPI converterá em um set e funcionará corretamente
# response_model_include=["name", "description"]
async def read_item_name(item_id: str) -> Item:
    return items[item_id]


@app.get("/item/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_name_public_data(item_id: str) -> Item:
    return items[item_id]


@app.post("/items/")
async def create_item(item: Item | list[Item]) -> list[Item]:
    return [each for each in item] if isinstance(item, list) else [item]


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID = None,
        start_datetime: datetime | None = Body(default=None),
        end_datetime: datetime | None = Body(default=None),
        repeat_at: time | None = Body(default=None),
        process_after: timedelta | None = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration
    }


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user


@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
