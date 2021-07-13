from fastapi_di_depends_issue import app
from fastapi_di_depends_issue.container import Container
from fastapi.testclient import TestClient
import pytest
import base64

container = Container()


@pytest.fixture()
def client() -> TestClient:
    container.wire(modules=[app])
    return TestClient(app.app)


def auth(username: str, password: str) -> str:
    plain = f"{username}:{password}".encode("ascii")
    encoded = base64.b64encode(plain).decode("ascii")
    return f"Basic {encoded}"


def test_fixed(client: TestClient):

    resp = client.get("/fixed", headers={"Authorization": auth("foo", "foo")})
    resp.raise_for_status()

    assert resp.json()["username"] == "foo"


def test_di(client: TestClient):

    resp = client.get("/with_di", headers={"Authorization": auth("bar", "bar")})
    resp.raise_for_status()
    assert resp.json()["username"] == "bar"


def test_di_workarround(client: TestClient):

    resp = client.get(
        "/with_di_workarround", headers={"Authorization": auth("bar", "bar")}
    )
    resp.raise_for_status()
    assert resp.json()["username"] == "bar"
