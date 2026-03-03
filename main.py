from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to FastAPI Docker App",
        "timestamp": datetime.utcnow()
    }

@app.get("/health")
def health_check():
    return {
        "status": "OK"
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User-{user_id}"
    }