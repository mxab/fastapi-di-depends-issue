
from fastapi_di_depends_issue import app
from fastapi_di_depends_issue.container import Container
from fastapi.testclient import TestClient
import pytest

container = Container()


@pytest.fixture()
def client()-> TestClient:
    container.wire(modules=[app])
    return TestClient(app.app)
    


def test_fixed(client: TestClient):
    
    resp = client.get("/fixed", headers={
        "Authorization": "Bearer 123"
    })
    resp.raise_for_status()
    
    assert resp.json()["user"] == "foo"


def test_di(client: TestClient):

    resp = client.get("/with_di", headers={
        "Authorization": "Bearer 123"
    })
    resp.raise_for_status()
    assert resp.json()["user"] == "bar"