from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_app.database import Base
from sql_app.main import get_db, app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def create_and_destroy_the_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def create_user():
    data = {
        "email": "amauri@gmail.com",
        "password": "1234"
    }
    response = client.post("/users/", json=data)
    return response


def create_item():
    data = {
        "title": "Um título para o user",
        "description": "Uma descrição do item do user"
    }
    response = client.post("/users/1/items/", json=data)
    return response


def test_get_users_status_code():
    create_and_destroy_the_database()
    response = client.get("/users/")
    assert response.status_code == 200


def test_get_users_json():
    create_and_destroy_the_database()
    response = client.get("/users/")
    assert response.json() == []


def test_get_user_status_code():
    create_and_destroy_the_database()
    create_user()
    response = client.get("/users/1")
    assert response.status_code == 200


def test_get_user_json():
    create_and_destroy_the_database()
    create_user()
    response = client.get("/users/1")
    assert response.json() == {
        "id": 1,
        "email": "amauri@gmail.com",
        "is_active": True,
        "items": [],
    }


def test_get_user_nonexistent_status_code():
    create_and_destroy_the_database()
    response = client.get("/users/1")
    assert response.status_code == 404


def test_get_user_nonexistent_json():
    create_and_destroy_the_database()
    response = client.get("/users/1")
    assert response.json() == {"detail": "User not found"}


def test_create_user_status_code():
    create_and_destroy_the_database()
    response = create_user()
    assert response.status_code == 201


def test_create_user_json():
    create_and_destroy_the_database()
    response = create_user()
    assert response.json() == {
        "id": 1,
        "email": "amauri@gmail.com",
        "is_active": True,
        "items": [],
    }


def test_read_items_empty_status_code():
    create_and_destroy_the_database()
    response = client.get("/items/")
    assert response.status_code == 200


def test_read_items_empty_json():
    create_and_destroy_the_database()
    response = client.get("/items/")
    assert response.json() == []


def test_create_item_for_user_status_code():
    create_and_destroy_the_database()
    create_user()
    response = create_item()
    assert response.status_code == 201


def test_create_item_for_user_json():
    create_and_destroy_the_database()
    create_user()
    response = create_item()
    assert response.json() == {
        "id": 1,
        "owner_id": 1,
        "title": "Um título para o user",
        "description": "Uma descrição do item do user"

    }


def test_create_item_json():
    create_and_destroy_the_database()
    create_user()
    response = create_item()
    assert response.json() == {
        "id": 1,
        "owner_id": 1,
        "title": "Um título para o user",
        "description": "Uma descrição do item do user"

    }


def test_read_items_json():
    create_and_destroy_the_database()
    create_user()
    create_item()
    response = client.get("/items/")
    assert response.json() == [{
        "id": 1,
        "owner_id": 1,
        "title": "Um título para o user",
        "description": "Uma descrição do item do user"

    }]
