'''
Instalação
==========
pip install fastapi
Também instale o uvicorn para funcionar como servidor:
pip install uvicorn

Para rodar o servidor:
uvicorn main:app --reload
Onde app é o nome do objeto de FastAPI()

Dica

Se você usa o PyCharm como seu editor, pode usar o plug-in Pydantic PyCharm .

Ele melhora o suporte do editor para modelos Pydantic, com:

autocompletar
verificações de tipo
reestruturação
procurando
inspeções
'''



from typing import List, Optional
from fastapi import FastAPI, Query, Path
from enum import Enum
from pydantic import BaseModel


class ModelName(str, Enum):
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
]

@app.get("/items/{item_id}")
async def read_user_item(item_id: int, needy: str, skip: int = 0, limit: int = 10, short: bool = False,
                        q: Optional[str] = Query(
                            None, 
                            min_length = 3, 
                            max_length=50,
                            title="Query string",
                            description="Query string for the items to search in the database that have a good match"
                            ), 
                        z: Optional[List[str]] = Query(
                            None,
                            alias="item-query"
                            ), 
                            regex="^fixedquery$"
                        ):
    """ FastAPI saberá que qé opcional por causa do = None.
    O Optionalin Optional[str]não é usado por FastAPI (FastAPI usará apenas a strparte), 
    mas Optional[str]permitirá que seu editor o ajude a encontrar erros em seu código. 

    Digamos que você queira declarar que o parâmetro q de consulta tem um min_length de 3 Se um valor padrão de "fixedquery":
    Query("fixedquery", min_length=3)

    Quando precisar declarar um valor conforme necessário durante o uso Query, você pode usar ...como o primeiro argumento:
    Query(..., min_length=3)
    O valor ... é um valor único especial, é parte do Python e é chamado de "Reticências".
    Isso permitirá que o FastAPI saiba que esse parâmetro é obrigatório.

    Você também pode usar list diretamente em vez de List[str]:
    async def read_items(q: list = Query([])):
    Neste caso, FastAPI não verificará o conteúdo da lista.
    Por exemplo, List[int]verificaria (e documentaria) se o conteúdo da lista são inteiros. Mas listsozinho não faria.
    """
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    if z:
        item.update({"z": z})
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some reiduals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query", deprecated=True)):
    """
    Imagine que você deseja que o parâmetro seja item-query.
    Como em: http://127.0.0.1:8000/items/?item-query=foobaritems
    Mas item-query não é um nome de variável Python válido. O mais próximo seria item_query.
    Você pode declarar um alias que será usado para encontrar o valor do parâmetro
    Se um parâmetro se tornar obsoleto, você tem que deixá-lo lá por um tempo porque há clientes usando-o, 
    mas você deseja que os documentos o mostrem claramente como obsoleto, passe o parâmetro deprecated=True para Query.
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items{item_id}")
async def update_item(
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000), 
        q: Optional[str] = None,
        item: Optional[Item] = None,
    ):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.put("/itemsdb/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


@app.get("/item/{id}")
async def read_item(*, id: int = Path(..., title="The ID of the item to get", ge=100), 
                    q: str, l: int = Query(..., lt=10), size: float = Query(..., gt=0, lt=1)):
    """
    Se você quiser declarar o parâmetro de consulta q sem Query nenhum valor padrão, e o parâmetro de caminho id 
    usando Path, e tê-los em uma ordem diferente, Python tem uma pequena sintaxe especial para isso.
    Passe *, como primeiro parâmetro da função.
    Python não fará nada com isso *, mas saberá que todos os parâmetros a seguir devem ser chamados como argumentos 
    de palavra-chave (pares de chave-valor), também conhecidos como kwargs. Mesmo que eles não tenham um valor padrão.
    Número de validações: 
        ge: greater than or equal (maior ou igual)
        gt: greater than (maior que)
        le: less than or equal (menor ou igual)
        lt: less than (menor que)
    O parâmetro size só será válido com números maiores que 0 e menores que 1, ou seja, 0.1, 0.2, 0.3333, 0.99999999)
    """
    results = {"id": id, "q": q, "l": l}
    return results


"""
Informações
===========

Query, PathE outros que você vai ver mais tarde são subclasses de um comum Paramclasse (que você não precisa para uso).
E todos eles compartilham os mesmos todos esses mesmos parâmetros de validação adicional e metadados que você viu.


Detalhes técnicos
=================

Quando você importa Query, Pathe outros de fastapi, eles são, na verdade, funções.
Que, quando chamado, retorna instâncias de classes com o mesmo nome.
Então, você importa Query, o que é uma função. E quando você o chama, ele retorna uma instância de uma classe também chamada Query.
Essas funções estão lá (em vez de apenas usar as classes diretamente) para que seu editor não marque erros sobre seus tipos.
Dessa forma, você pode usar seu editor normal e ferramentas de codificação sem ter que adicionar configurações personalizadas para ignorar esses erros.
"""
