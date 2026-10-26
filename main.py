
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Sensor(BaseModel):
    tag: str
    valor: float

@app.get("/")
def home():
    return {"mensaje": "API funcionando"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/sensores")
def recibir_sensor(sensor: Sensor):
    return {
        "mensaje": "Sensor recibido",
        "data": sensor.model_dump()
    }
