import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.fastapi.app import get_fastapi_app

@pytest.fixture(scope='module')
def client() -> FastAPI:
    return TestClient(get_fastapi_app())


