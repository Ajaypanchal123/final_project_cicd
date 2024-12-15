import pytest
from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"Welcome to the Web Application!"

def test_api():
    client = app.test_client()
    response = client.get('/api')
    assert response.json == {"message": "Hello from the API!"}
