from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from operations import add, subtract, multiply, divide
from app.routes_user import router as user_router
from app.routes_calculation import router as calculation_router
from app.database import Base, engine
from app.models import user, calculation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(calculation_router)

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