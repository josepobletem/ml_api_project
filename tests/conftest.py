import pytest
from fastapi.testclient import TestClient
from api.main import app

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

@pytest.fixture(scope="module")
def auth_token(client):
    response = client.get("/token")
    token = response.json()["access_token"]
    return f"Bearer {token}"

@pytest.fixture(scope="function")
def headers(auth_token):
    return {"Authorization": auth_token}
