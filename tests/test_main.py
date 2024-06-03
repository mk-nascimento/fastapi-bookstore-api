from http import HTTPStatus

from fastapi.testclient import TestClient


def test_should_be_null(client: TestClient):
    res = client.get('/')
    assert res.status_code == HTTPStatus.OK
    assert not res.json()


def test_should_redirect_and_null(client: TestClient):
    res = client.get('/health')
    assert res.status_code == HTTPStatus.OK
    assert not res.json()
