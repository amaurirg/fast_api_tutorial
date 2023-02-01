from fastapi.testclient import TestClient
from app.form import app

client = TestClient(app)


# Form
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


'''
# File / UploadFile
def test_create_file_status_code():
    files = {"upload-file": open("/home/amauri/Downloads/GeradorRelatório Gerador Reserve_17-01-2023.xls", "rb")}
    response = client.post("/files/", files=files)
    assert response.status_code == 200


def test_upload_file_status_code():
#     files = {"upload-file": open("/home/amauri/Downloads/GeradorRelatório Gerador Reserve_17-01-2023.xls", "rb")}
    files = {"upload-file": (
        "report.xls", open("/home/amauri/Downloads/GeradorRelatório Gerador Reserve_17-01-2023.xls", "rb"),
        "application/vnd.ms-excel")}
    response = client.post("/uploadfile/", files=files)
    assert response.status_code == 200
    # assert response.json() == {}
'''
