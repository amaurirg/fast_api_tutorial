from datetime import datetime

from fastapi.testclient import TestClient

from app.extra_fields import app

client = TestClient(app)


# Some types

# GET
# url = "/items/{item_id}"


# PUT
# url = "/items/{item_id}"
def test_read_items_status_code():
    data = {
        "item_id": "12e9dcc7-133c-4b42-b82d-a420c63e036e",
        "start_datetime": "2023-01-20T04:21:00",
        "end_datetime": "2023-01-25T09:45:00",
        "repeat_at": "11:32:57",
        "process_after": "2",
    }
    response = client.put("/items/12e9dcc7-133c-4b42-b82d-a420c63e036e", json=data)
    assert response.status_code == 200


def test_read_items_json():
    end_datetime = datetime(2023, 1, 25, 9, 45).isoformat()
    data = {
        # "item_id": "12e9dcc7-133c-4b42-b82d-a420c63e036e",
        "start_datetime": "2023-01-20T04:21:00",
        # "end_datetime": "2023-01-25T09:45:00",
        "end_datetime": end_datetime,
        "repeat_at": "11:32:57",
        "process_after": "2",
    }
    response = client.put("/items/12e9dcc7-133c-4b42-b82d-a420c63e036e", json=data)
    assert response.json() == {
        "duration": 451438.0,
        # "end_datetime": "2023-01-25T09:45:00",
        "end_datetime": end_datetime,
        "item_id": "12e9dcc7-133c-4b42-b82d-a420c63e036e",
        "process_after": 2.0,
        "repeat_at": "11:32:57",
        "start_datetime": "2023-01-20T04:21:00",
        "start_process": "2023-01-20T04:21:02"
    }


# GET
# url = "/item/{item_id}"
def test_read_item_status_code():
    response = client.get("/item/bar")
    assert response.status_code == 200


def test_read_item_bar_json():
    response = client.get("/item/bar")
    assert response.json() == {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2
    }


def test_read_item_foo_json():
    response = client.get("/item/foo")
    assert response.json() == {
        "name": "Foo",
        "price": 50.2
    }


def test_read_item_baz_foo_json():
    response = client.get("/item/baz")
    assert response.json() == {
        "name": "Baz",
        "price": 50.2,
        "tax": 10.5,
        "tags": []
    }


# url = "/item/{item_id}/name"
def test_read_item_name_status_code():
    response = client.get("/item/bar/name")
    assert response.status_code == 200


def test_read_item_name_json():
    response = client.get("/item/bar/name")
    assert response.json() == {
        "name": "Bar",
        "description": "The bartenders"
    }


def test_read_item_public_data_status_code():
    response = client.get("/item/bar/public")
    assert response.status_code == 200


def test_read_item_public_data_json():
    response = client.get("/item/baz/public")
    assert response.json() == {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tags": []
    }


# POST
# url = "/items/datetime/"
def test_datetime_status_code():
    current_time = datetime.now().time().isoformat()
    current_date = datetime.now().isoformat()
    data = {
        "birth_date": datetime(1974, 10, 31).date().isoformat(),
        "current_time": current_time,
        "current_date": current_date
    }
    response = client.post("/items/datetime/", json=data)
    assert response.status_code == 200
    # assert response.json() == {}


def test_datetime_json():
    birth_date = datetime(1974, 10, 31).date().isoformat()
    current_time = datetime.now().time().isoformat()
    current_date = datetime.now().isoformat()
    data = {
        "birth_date": birth_date,
        "current_time": current_time,
        "current_date": current_date
    }
    response = client.post("/items/datetime/", json=data)
    assert response.json() == {
        "birth_date": "1974-10-31",
        "current_time": current_time,
        "current_date": current_date
    }


def test_uuid_json():
    data = {"id": "12e9dcc7-133c-4b42-b82d-a420c63e036e"}
    response = client.post("/items/uuid/", json=data)
    assert response.json() == {"id": "12e9dcc7-133c-4b42-b82d-a420c63e036e"}


def test_bad_uuid_status_code():
    data = {"id": "1"}
    response = client.post("/items/uuid/", json=data)
    assert response.status_code == 422


def test_bad_uuid_json():
    data = {"id": "1"}
    response = client.post("/items/uuid/", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'id'],
                'msg': 'value is not a valid uuid',
                'type': 'type_error.uuid'
            }
        ]
    }


# url = "/items/list/"
def test_item_list_status_code():
    response = client.get("/items/list/")
    assert response.status_code == 200


def test_item_list_json():
    response = client.get("/items/list/")
    assert response.json() == [
        {
            "name": "Portal Gun",
            "description": None,
            "price": 42,
            "tax": 10.5,
            "tags": []
        },
        {
            "name": "Plumbus",
            "description": None,
            "price": 32,
            "tax": 10.5,
            "tags": []
        }
    ]


def test_create_item():
    data = {
        "name": "Python Fluent",
        "price": 157,
    }
    response = client.post("/items/", json=data)
    assert response.json() == [
        {
            "name": "Python Fluent",
            "description": None,
            "price": 157,
            "tax": 10.5,
            "tags": []
        }
    ]


def test_create_item_list():
    data = [
        {
            "name": "Python Fluent",
            "price": 157,
        },
        {
            "name": "Python Cookbook",
            "price": 113,
        }
    ]
    response = client.post("/items/", json=data)
    assert response.json() == [
        {
            "name": "Python Fluent",
            "description": None,
            "price": 157,
            "tax": 10.5,
            "tags": []
        }, {
            "name": "Python Cookbook",
            "description": None,
            "price": 113,
            "tax": 10.5,
            "tags": []
        }
    ]


def test_userin_status_code():
    data = {
        "username": "amaurirg",
        "password": "1234",
        "email": "amauri@gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }
    response = client.post("/user/", json=data)
    assert response.status_code == 200


def test_userin_json():
    data = {
        "username": "amaurirg",
        "password": "1234",
        "email": "amauri@gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }
    response = client.post("/user/", json=data)
    assert response.json() == {
        "username": "amaurirg",
        "email": "amauri@gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }


def test_bad_userin_json():
    data = {
        "username": "amaurirg",
        "password": "1234",
        "email": "amauri.gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }
    response = client.post("/user/", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'email'],
                'msg': 'value is not a valid email address',
                'type': 'value_error.email'
            }
        ]
    }


def test_userout_status_code():
    data = {
        "username": "amaurirg",
        "password": "1234",
        "email": "amauri@gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }
    response = client.post("/user/", json=data)
    assert response.status_code == 200


def test_userout_json():
    data = {
        "username": "amaurirg",
        "password": "1234",
        "email": "amauri@gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }
    response = client.post("/user/", json=data)
    assert response.json() == {
        "username": "amaurirg",
        "email": "amauri@gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }


def test_bad_userout_json():
    data = {
        "username": "amaurirg",
        "password": "1234",
        "email": "amauri.gmail.com",
        "full_name": "Amauri Rossetti Giovani"
    }
    response = client.post("/user/", json=data)
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'email'],
                'msg': 'value is not a valid email address',
                'type': 'value_error.email'
            }
        ]
    }


# GET
# url = "/portal"
def test_portal_jsonresponse_status_code():
    response = client.get("/portal")
    assert response.status_code == 200


def test_portal_jsonresponse_json():
    response = client.get("/portal")
    assert response.json() == {
        "message": "Here's your interdimensional portal."
    }

# REDIRECT

# def test_portal_redirect_status_code():
#     response = client.get("/portal?teleport=true")
#     assert response.status_code == 307


# def test_teleport_status_code():
#     response = client.get("/teleport")
#     assert response.status_code == 200
