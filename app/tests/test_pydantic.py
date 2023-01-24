from datetime import datetime

from fastapi.testclient import TestClient

from app.pydantic_start import app

client = TestClient(app)


# url = "/items/"
def test_get_items_add_date_now():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}")
    assert response.json() == {"date_now": date_now, "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}


def test_get_items_add_without_date_now():
    response = client.get(f"/items/")
    assert response.json() == {
        'detail': [
            {
                'loc': ['query', 'date_now'],
                'msg': 'field required',
                'type': 'value_error.missing'
            }
        ]
    }


def test_get_items_status_code():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}")
    assert response.status_code == 200


def test_get_items_json():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}")
    assert response.json() == {"date_now": date_now, "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}


def test_get_items_add_q_empty():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=")
    assert response.json() == {
        'detail': [
            {
                'loc': ['query', 'q'],
                'msg': 'ensure this value has at least 3 characters',
                'type': 'value_error.any_str.min_length',
                'ctx': {'limit_value': 3}
            }
        ]
    }


def test_get_items_add_q_status_code():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=teste")
    assert response.status_code == 200


def test_get_items_add_q_len():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=teste")
    assert len(response.json()) == 3


def test_get_items_add_q_json():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=teste")
    assert response.json() == {"date_now": date_now, "items": [{"item_id": "Foo"}, {"item_id": "Bar"}], "q": "teste"}


def test_get_items_add_q_greater_than_5_status_code():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=testes")
    assert response.status_code == 422


def test_get_items_add_q_greater_than_5_len():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=testes")
    assert len(response.json()) == 1


def test_get_items_add_q_greater_than_5_json():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=testes")
    assert response.json() == {
        'detail': [
            {
                'loc': ['query', 'q'],
                'msg': 'ensure this value has at most 5 characters',
                'type': 'value_error.any_str.max_length',
                'ctx': {'limit_value': 5}
            }
        ]
    }


def test_get_items_add_q_less_than_3():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=te")
    assert response.json() == {
        'detail': [
            {
                'loc': ['query', 'q'],
                'msg': 'ensure this value has at least 3 characters',
                'type': 'value_error.any_str.min_length',
                'ctx': {'limit_value': 3}
            }
        ]
    }


def test_get_items_add_q_regex_true():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=teste")
    assert response.json() == {"date_now": date_now, "items": [{"item_id": "Foo"}, {"item_id": "Bar"}], "q": "teste"}


def test_get_items_add_q_regex_false():
    date_now = datetime.now().strftime("%d/%m/%Y-%H:%M")
    response = client.get(f"/items/?date_now={date_now}&q=test1")
    assert response.json() == {
        'detail': [
            {
                'loc': ['query', 'q'],
                'msg': 'string does not match regex "^teste$"',
                'type': 'value_error.str.regex',
                'ctx': {'pattern': '^teste$'}
            }
        ]
    }


# GET
# url = "/new-items/"
def test_get_new_items_status_code():
    response = client.get("/new-items/")
    assert response.status_code == 200


def test_get_new_items_json():
    response = client.get("/new-items/")
    assert response.json() == {"q": None}


def test_get_items_add_q_multiple_times_json():
    response = client.get("/new-items/?item-query=test1&item-query=test2")
    assert response.json() == {"q": ["test1", "test2"]}


def test_get_new_items_item_query_status_code():
    response = client.get("/new-items/?item-query=teste")
    assert response.status_code == 200


def test_get_new_items_item_query_json():
    response = client.get("/new-items/?item-query=teste")
    assert response.json() == {'q': ["teste"]}


# POST
# url = "/new-items/"
def test_post_items():
    data = {
        "name": "teste2",
        "description": "testando post",
        "price": 103,
        "tax": 32
    }
    response = client.post("/items/", json=data)
    assert response.status_code == 200


def test_post_items_with_tax():
    data = {
        "name": "teste2",
        "description": "testando post",
        "price": 103,
        "tax": 32
    }
    response = client.post("/items/", json=data)
    assert 'price_with_tax' in response.json()
    assert response.json()['price_with_tax'] == 135.0


# PUT
# url = "/items/{item_id}"
def test_put_item():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/5", json=data)
    assert response.status_code == 200


def test_update_item_bad_str_status_code():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/teste", json=data)
    assert response.status_code == 422


def test_update_item_bad_str_json():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/teste", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['path', 'item_id'],
                'msg': 'value is not a valid integer',
                'type': 'type_error.integer'
            }
        ]
    }


def test_update_item_bad_float_status_code():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/3.5", json=data)
    assert response.status_code == 422


def test_update_item_bad_float_json():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/3.5", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['path', 'item_id'],
                'msg': 'value is not a valid integer',
                'type': 'type_error.integer'
            }
        ]
    }


def test_update_item_bad_tuple_status_code():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/3,5", json=data)
    assert response.status_code == 422


def test_update_item_bad_tuple_json():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/3,5", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['path', 'item_id'],
                'msg': 'value is not a valid integer',
                'type': 'type_error.integer'
            }
        ]
    }


def test_update_item_bad_list_status_code():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/[3, 5]", json=data)
    assert response.status_code == 422


def test_update_item_bad_list_json():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/[3, 5]", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['path', 'item_id'],
                'msg': 'value is not a valid integer',
                'type': 'type_error.integer'
            }
        ]
    }


def test_update_item_less_than_5_status_code():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/1", json=data)
    assert response.status_code == 422


def test_update_item_less_than_5_json():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/1", json=data)
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 5},
                'loc': ['path', 'item_id'],
                'msg': 'ensure this value is greater than or equal to 5',
                'type': 'value_error.number.not_ge'
            }
        ]
    }


def test_update_item_greater_than_10_status_code():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/11", json=data)
    assert response.status_code == 422


def test_update_item_greater_than_10_json():
    data = {
        "name": "teste2",
        "description": "testando put",
        "price": 452,
        "tax": 43
    }
    response = client.put("/items/11", json=data)
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 10},
                'loc': ['path', 'item_id'],
                'msg': 'ensure this value is less than or equal to 10',
                'type': 'value_error.number.not_le'
            }
        ]
    }


# PUT
# url = "/new-items/{item_id}"
def test_update_new_item_status_code():
    data = {
        "item": {
            "name": "teste2",
            "description": "testando put",
            "price": 452,
            "tax": 43
        },
        "user": {
            "username": "amaurirg",
            "full_name": "Amauri Rossetti Giovani"
        },
        "importance": 5
    }
    response = client.put("/new-items/1", json=data)
    assert response.status_code == 200


def test_update_new_item_json():
    data = {
        "item": {
            "name": "teste2",
            "description": "testando put",
            "price": 452,
            "tax": 43
        },
        "user": {
            "username": "amaurirg",
            "full_name": "Amauri Rossetti Giovani"
        },
        "importance": 5
    }
    response = client.put("/new-items/1", json=data)
    assert response.json() == {
        "item_id": 1,
        "item": {
            "name": "teste2",
            "description": "testando put",
            "price": 452,
            "tax": 43
        },
        "user": {
            "username": "amaurirg",
            "full_name": "Amauri Rossetti Giovani"
        },
        "importance": 5
    }


def test_update_new_item_without_data_status_code():
    response = client.put("/new-items/")
    assert response.status_code == 405


def test_update_new_item_without_data_json():
    response = client.put("/new-items/")
    assert response.json() == {'detail': 'Method Not Allowed'}


def test_update_new_item_without_importance_status_code():
    data = {
        "item": {
            "name": "teste2",
            "description": "testando put",
            "price": 452,
            "tax": 43
        },
        "user": {
            "username": "amaurirg",
            "full_name": "Amauri Rossetti Giovani"
        },
    }
    response = client.put("/new-items/1", json=data)
    assert response.status_code == 422


def test_update_new_item_without_importance_json():
    data = {
        "item": {
            "name": "teste2",
            "description": "testando put",
            "price": 452,
            "tax": 43
        },
        "user": {
            "username": "amaurirg",
            "full_name": "Amauri Rossetti Giovani"
        },
    }
    response = client.put("/new-items/1", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'importance'],
                'msg': 'field required',
                'type': 'value_error.missing'
            }
        ]
    }


# POST
# url = "/new-items/"
def test_create_new_item():
    data = {
        "item": {
            "name": "teste2",
            "description": "testando post",
            "price": 103,
            "tax": 32
        }
    }
    response = client.post("/new-items/", json=data)
    assert response.json() == {
        "item_id": 1,
        "item": {
            "name": "teste2",
            "description": "testando post",
            "price": 103,
            "tax": 32
        }
    }


# GET
# url = "/products/"
def test_get_products_status_code():
    response = client.get("/products/")
    assert response.status_code == 200


def test_get_products_json():
    response = client.get("/products/")
    assert response.json() == {
        "products": [
            {
                "name": "Carro",
                "description": "Descrição do carro",
                "price": 15000.00,
                "tax": 1500.00
            }
        ]
    }


# POST
# url = "/products/create/"
def test_post_create_product_status_code():
    data = {
        "name": "TV",
        "description": "Descrição da TV",
        "price": 2300.00,
        "tax": 230.00
    }
    response = client.post("/products/create/", json=data)
    assert response.status_code == 200


def test_create_product_json():
    data = {
        "name": "TV",
        "description": "Descrição da TV",
        "price": 2300.00,
        "tax": 230.00,
        "key_words": ["TV", "Smart", "Full HD"],
        "image": [{
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }]
    }
    response = client.post("/products/create/", json=data)
    assert response.json() == {
        "products": [
            {
                "name": "Carro",
                "description": "Descrição do carro",
                "price": 15000.00,
                "tax": 1500.00,
            },
            {
                "name": "TV",
                "description": "Descrição da TV",
                "price": 2300.00,
                "tax": 230.00,
                "key_words": ["TV", "Smart", "Full HD"],
                "image": [{
                    "url": "http://example.com/baz.jpg",
                    "name": "The Foo live"
                }]
            }
        ]
    }


def test_create_product_with_non_existent_field_json():
    data = {
        "name": "TV",
        "description": "Descrição da TV",
        "price": 2300.00,
        "tax": 230.00,
        "color": "black"
    }
    response = client.post("/products/create/", json=data)
    assert response.json() == {
        "products": [
            {
                "name": "Carro",
                "description": "Descrição do carro",
                "price": 15000.00,
                "tax": 1500.00
            },
            {
                "name": "TV",
                "description": "Descrição da TV",
                "price": 2300.00,
                "tax": 230.00,
                "key_words": [],
                "image": None
            }
        ]
    }


def test_create_product_without_price_json():
    data = {
        "name": "TV",
        "description": "Descrição da TV",
        "tax": 230.00,
        "image": [{
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }]
    }
    response = client.post("/products/create/", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'price'],
                'msg': 'field required',
                'type': 'value_error.missing'
            }
        ]
    }


def test_bad_create_product_json():
    data = [
        "TV",
        "Descrição da TV",
        2300.00,
        230.00
    ]
    response = client.post("/products/create/", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['body'],
                'msg': 'value is not a valid dict',
                'type': 'type_error.dict'
            }
        ]
    }


def test_create_product_bad_price_and_tax_json():
    data = {
        "name": "TV",
        "description": "Descrição da TV",
        "price": "2300,00",
        "tax": "230,00",
        "image": [{
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }]
    }
    response = client.post("/products/create/", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'price'],
                'msg': 'value is not a valid float',
                'type': 'type_error.float'
            },
            {
                'loc': ['body', 'tax'],
                'msg': 'value is not a valid float',
                'type': 'type_error.float'
            }
        ]
    }


def test_create_product_description_bad_size_status_code():
    data = {
        "name": "TV",
        "description": "Smart TV LED Full HD com Wi-fi, Entradas HDMI e USB",
        "price": 2300.00,
        "tax": 230.00
    }
    response = client.post("/products/create/", json=data)
    assert response.status_code == 422


def test_create_product_description_bad_size_json():
    data = {
        "name": "TV",
        "description": "Smart TV LED Full HD com Wi-fi, Entradas HDMI e USB",
        "price": 2300.00,
        "tax": 230.00
    }
    response = client.post("/products/create/", json=data)
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 30},
                'loc': ['body', 'description'],
                'msg': 'ensure this value has at most 30 characters',
                'type': 'value_error.any_str.max_length'
            }
        ]
    }


def test_create_product_with_image_json():
    data = {
        "name": "TV",
        "description": "Descrição da TV",
        "price": 2300.00,
        "tax": 230.00,
        "key_words": ["TV", "Smart", "Full HD"],
        "image": [{
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }]
    }
    response = client.post("/products/create/", json=data)
    assert response.json() == {
        "products": [
            {
                "name": "Carro",
                "description": "Descrição do carro",
                "price": 15000.00,
                "tax": 1500.00,
            },
            {
                "name": "TV",
                "description": "Descrição da TV",
                "price": 2300.00,
                "tax": 230.00,
                "key_words": ["TV", "Smart", "Full HD"],
                "image": [{
                    "url": "http://example.com/baz.jpg",
                    "name": "The Foo live"
                }]
            }
        ]
    }


def test_create_product_with_bad_url_image_json():
    data = {
        "name": "TV",
        "description": "Descrição da TV",
        "price": 2300.00,
        "tax": 230.00,
        "key_words": ["TV", "Smart", "Full HD"],
        "image": [{
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
            {
                "url": "http://example",
                "name": "The Foo live"
            }
        ]
    }
    response = client.post("/products/create/", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'image', 1, 'url'],
                'msg': 'URL host invalid, top level domain required',
                'type': 'value_error.url.host'
            }
        ]
    }
