import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from main import app
from app.database import Base, get_db
from app.models import user, calculation  # makes sure models are loaded

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with TestClient(app) as test_client:
        yield test_client

    Base.metadata.drop_all(bind=engine)


def test_register_user(client):
    response = client.post(
        "/users/register",
        json={
            "username": "kavya",
            "email": "kavya@test.com",
            "password": "1234"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "kavya"
    assert data["email"] == "kavya@test.com"
    assert "id" in data


def test_login_user(client):
    client.post(
        "/users/register",
        json={
            "username": "kavya",
            "email": "kavya@test.com",
            "password": "1234"
        }
    )

    response = client.post(
        "/users/login",
        json={
            "username": "kavya",
            "email": "kavya@test.com",
            "password": "1234"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"


def test_create_calculation(client):
    response = client.post(
        "/calculations",
        json={
            "a": 10,
            "b": 5,
            "type": "Add"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["a"] == 10
    assert data["b"] == 5
    assert data["type"] == "Add"
    assert data["result"] == 15


def test_get_all_calculations(client):
    client.post(
        "/calculations",
        json={
            "a": 10,
            "b": 5,
            "type": "Add"
        }
    )

    response = client.get("/calculations")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1


def test_get_calculation_by_id(client):
    create_response = client.post(
        "/calculations",
        json={
            "a": 20,
            "b": 4,
            "type": "Divide"
        }
    )

    calc_id = create_response.json()["id"]

    response = client.get(f"/calculations/{calc_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == calc_id
    assert data["result"] == 5


def test_update_calculation(client):
    create_response = client.post(
        "/calculations",
        json={
            "a": 8,
            "b": 2,
            "type": "Multiply"
        }
    )

    calc_id = create_response.json()["id"]

    response = client.put(
        f"/calculations/{calc_id}",
        json={
            "a": 20,
            "b": 4,
            "type": "Divide"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["a"] == 20
    assert data["b"] == 4
    assert data["type"] == "Divide"
    assert data["result"] == 5


def test_delete_calculation(client):
    create_response = client.post(
        "/calculations",
        json={
            "a": 7,
            "b": 3,
            "type": "Add"
        }
    )

    calc_id = create_response.json()["id"]

    delete_response = client.delete(f"/calculations/{calc_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Calculation deleted successfully"

    get_response = client.get(f"/calculations/{calc_id}")
    assert get_response.status_code == 404


def test_invalid_calculation_type(client):
    response = client.post(
        "/calculations",
        json={
            "a": 10,
            "b": 5,
            "type": "WrongType"
        }
    )

    assert response.status_code == 422


def test_divide_by_zero(client):
    response = client.post(
        "/calculations",
        json={
            "a": 10,
            "b": 0,
            "type": "Divide"
        }
    )

    assert response.status_code == 422