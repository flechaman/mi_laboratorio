from fastapi import FastAPI
from db import test_connection

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/db")
def db_check():
    result = test_connection()
    return {"database": result}
