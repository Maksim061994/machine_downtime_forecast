import requests



def default_check_data(response: requests.Response, data_len: int = 100) -> None:
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) == data_len


def get_token(client):
    response = client.post("/users/login", json={"login": "login", "password": "pass"})
    data = response.json()
    return data["token"]

