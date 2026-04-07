from fastapi import FastAPI
from app.routes.api import api_router


app = FastAPI(title="ATM Management", version="1.0.0")
app.include_router(api_router)


@app.get("/")
def home():
    return {"status": True, "message" : "FastAPI Project is Running...."}