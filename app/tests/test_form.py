from fastapi import Form
from fastapi.testclient import TestClient
from app.form import app

client = TestClient(app)


def test_form_status_code():
    data = {
        "username": "amaurirg",
        "password": "1234"
    }
    response = client.post("/login/", data=data)
    assert response.status_code == 200


def test_form_json():
    data = {
        "username": "amaurirg",
        "password": "1234"
    }
    response = client.post("/login/", data=data)
    assert response.json() == {
        "username": "amaurirg",
    }


# def test_create_file_status_code():
#     files = {"upload-file": open("/home/amauri/Downloads/GeradorRelatório Gerador Reserve_17-01-2023.xls", "rb")}
#     response = client.post("/files/", files=files)
#     assert response.status_code == 200


# def test_create_file_json():
#     files = {"upload-file": open("/home/amauri/Downloads/GeradorRelatório Gerador Reserve_17-01-2023.xls", "rb")}
#     response = client.post("/files/", files=files)
#     assert response.json() == {}
