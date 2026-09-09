import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["application"] == "student-ml-api"
    assert response.json()["version"] == "1.0.0"


def test_predict_success():
    response = client.post("/predict", json={"value": 10})

    assert response.status_code == 200
    assert response.json() == {
        "input": 10.0,
        "prediction": 20.0
    }


def test_predict_missing_input():
    response = client.post("/predict", json={})

    assert response.status_code == 422


def test_predict_invalid_input():
    response = client.post("/predict", json={"value": "invalid"})

    assert response.status_code == 422
