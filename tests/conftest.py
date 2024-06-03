import pytest
from fastapi.testclient import TestClient

from bookstore.main import app


@pytest.fixture()
def client():
    return TestClient(app)
