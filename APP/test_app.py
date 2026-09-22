from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Banking Account Service is running"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "UP"


def test_get_accounts():
    client = app.test_client()

    response = client.get("/accounts")

    assert response.status_code == 200
    assert len(response.json) == 2


def test_get_existing_account():
    client = app.test_client()

    response = client.get("/accounts/101")

    assert response.status_code == 200
    assert response.json["customer"] == "John"
    assert response.json["balance"] == 50000


def test_get_nonexistent_account():
    client = app.test_client()

    response = client.get("/accounts/999")

    assert response.status_code == 404
    assert response.json["error"] == "Account not found"