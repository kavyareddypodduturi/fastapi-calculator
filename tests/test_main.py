from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Calculator API is running"}

def test_add_endpoint():
    response = client.get("/add?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}

def test_subtract_endpoint():
    response = client.get("/subtract?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_multiply_endpoint():
    response = client.get("/multiply?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 50.0}

def test_divide_endpoint():
    response = client.get("/divide?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}