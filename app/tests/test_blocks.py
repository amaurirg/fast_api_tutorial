from typing import Dict, Any, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field, root_validator
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


class InnerBlock(BaseModel):
    field1: Optional[str] = None
    field2: Optional[int] = None

    # Pré-processamento para substituir dicionário vazio por None
    @root_validator(pre=True)
    def replace_empty_dict(cls, values):
        if not values:
            return None
        return values

class OuterBlock(BaseModel):
    block1: Optional[InnerBlock] = Field(default_factory=dict)
    block2: Optional[InnerBlock] = Field(default_factory=dict)


@app.post("/nested_blocks/")
async def process_nested_blocks(blocks: OuterBlock):
    return blocks

def test_blocks_status_code():
    data = {}
    response = client.post("/nested_blocks/", json=data)
    assert response.status_code == 200


def test_blocks_json():
    data = {}
    response = client.post("/nested_blocks/", json=data)
    assert response.json() == {}
