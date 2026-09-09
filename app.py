from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="student-ml-api")


class PredictionInput(BaseModel):
    value: float


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": "1.0.0"
    }


@app.post("/predict")
def predict(data: PredictionInput):
    return {
        "input": data.value,
        "prediction": data.value * 2
    }
