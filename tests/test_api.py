from fastapi.testclient import TestClient
from api.app import app
import sys
import os

sys.path.append(os.getcwd())


client = TestClient(app)

def test_api():
    response = client.post("/analyze", json={
        "resume": "Python ML engineer",
        "jd": "Looking for Python, Docker"
    })
    assert response.status_code == 200