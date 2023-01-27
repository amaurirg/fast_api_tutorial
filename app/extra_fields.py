from datetime import datetime, timedelta, time, date
from typing import Union
from uuid import UUID

from fastapi import FastAPI, Body, Cookie
from pydantic import BaseModel

app = FastAPI()


class DatetimeModel(BaseModel):
    birth_date: date
    current_time: time
    current_date: datetime

class UuidModel(BaseModel):
    id: UUID = None


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID = None,
        start_datetime: Union[datetime, None] = Body(default=None),
        end_datetime: Union[datetime, None] = Body(default=None),
        repeat_at: Union[time, None] = Body(default=None),
        process_after: Union[timedelta, None] = Body(default=None),
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


@app.post("/items/datetime/")
async def items_datetime(item: DatetimeModel):
    return {
        "birth_date": item.birth_date,
        "current_time": item.current_time,
        "current_date": item.current_date
    }


@app.post("/items/uuid/")
async def item_uuid(item: UuidModel):
    return {"id": item.id}


@app.get("/items/cookies/")
async def item_cookies(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}
