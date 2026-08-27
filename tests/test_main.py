from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee API is running successfully"
    }


def test_get_employees():
    response = client.get("/employees")

    assert response.status_code == 200

    employees = response.json()

    assert len(employees) == 3
    assert employees[0]["name"] == "John"