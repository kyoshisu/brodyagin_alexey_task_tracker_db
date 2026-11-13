from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code in [200, 400]


def test_login_and_create_task():
    login_data = {"username": "testuser", "password": "testpassword"}
    response = client.post("/token", data=login_data)
    assert response.status_code == 200
    token = response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    task_data = {"title": "My Test Task", "description": "Testing", "status": "new"}
    response = client.post("/tasks/", json=task_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "My Test Task"


def test_get_tasks():
    login_data = {"username": "testuser", "password": "testpassword"}
    token = client.post("/token", data=login_data).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/tasks/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)