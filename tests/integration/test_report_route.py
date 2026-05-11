from fastapi.testclient import TestClient
from main import app
from app.database import get_db


class FakeQuery:
    def filter(self, *args, **kwargs):
        return self

    def count(self):
        return 0

    def scalar(self):
        return 0


class FakeDB:
    def query(self, *args, **kwargs):
        return FakeQuery()


def override_get_db():
    yield FakeDB()


def test_get_calculation_stats():
    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)
    response = client.get("/calculations/stats/report")

    app.dependency_overrides.clear()

    assert response.status_code == 200

    data = response.json()

    assert "total_calculations" in data
    assert "total_add_operations" in data
    assert "total_subtract_operations" in data
    assert "highest_result" in data
    assert "average_result" in data