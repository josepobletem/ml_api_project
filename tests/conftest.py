import pytest
from fastapi.testclient import TestClient

from api.main import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture(scope="module")
def auth_token(client):
    response = client.post("/token")
    print("DEBUG /token response:", response.status_code, response.text)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data, f"No access_token in response: {data}"
    return data["access_token"]


@pytest.fixture(scope="function")
def headers(auth_token):
    return {"Authorization": auth_token}
