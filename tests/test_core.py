from urllib import response
from fastapi.testclient import TestClient
from scripts.api.app import app

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Instructions': 'Type [/docs] after the localhost address for viewing the Swagger UI'}
