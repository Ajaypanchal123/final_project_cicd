import pytest
from app import app  # Simplified import

import sys
import os

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_api(client):
    response = client.get("/api")
    assert response.json == {"message": "Hello from Flask API"}
