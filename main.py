from fastapi import FastAPI
from operations import add, subtract, multiply, divide

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Calculator API is running"}

@app.get("/add")
def add_numbers(a: float, b: float):
    return {"result": add(a, b)}

@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    return {"result": subtract(a, b)}

@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    return {"result": multiply(a, b)}

@app.get("/divide")
def divide_numbers(a: float, b: float):
    return {"result": divide(a, b)}