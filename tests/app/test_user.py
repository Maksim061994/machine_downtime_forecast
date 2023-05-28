from fastapi.testclient import TestClient

from app.main import app
from tests.app.utils import get_token

client = TestClient(app)
TOKEN = get_token(client)


def test_users_login():
    response = client.post("/users/login", json={"login": "user", "password": "pass"})
    assert response.status_code == 200
    assert "token" in response.json()

