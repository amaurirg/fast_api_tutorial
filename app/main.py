from typing import Union, Dict, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool]

@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None) -> Dict:
    return {'item_id': item_id, 'q': q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item) -> Dict:
    return {'item_name': item.name, 'item_id': item_id, 'item_is_offer': item.is_offer}
