from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main() -> None:
    response: TestClient = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello from Fastapi!"
