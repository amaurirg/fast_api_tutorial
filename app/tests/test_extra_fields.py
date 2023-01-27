import uuid
from datetime import datetime, time, timedelta
from uuid import uuid4, UUID

from fastapi.testclient import TestClient

from app.extra_fields import app

client = TestClient(app)


# Some types
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


# POST
# url = "/items/{item_id}"

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
    # response = client.put("/items/{}".format(uuid.uuid4()), json=data)
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
