import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_biomas():
    response = client.get("/biomas")
    assert response.status_code == 200
    assert "biomas" in response.json()
