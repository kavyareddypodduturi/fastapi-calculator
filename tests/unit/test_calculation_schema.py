from pydantic import ValidationError
from app.schemas.calculation import CalculationCreate, CalculationRead


def test_calculation_create_valid_add():
    calc = CalculationCreate(a=10, b=5, type="Add")
    assert calc.a == 10
    assert calc.b == 5
    assert calc.type == "Add"


def test_calculation_create_valid_divide():
    calc = CalculationCreate(a=10, b=2, type="Divide")
    assert calc.type == "Divide"
    assert calc.b == 2


def test_calculation_create_invalid_type():
    try:
        CalculationCreate(a=10, b=5, type="Power")
        assert False
    except ValidationError as e:
        assert "type must be Add, Sub, Multiply, or Divide" in str(e)


def test_calculation_create_divide_by_zero():
    try:
        CalculationCreate(a=10, b=0, type="Divide")
        assert False
    except ValidationError as e:
        assert "Division by zero is not allowed" in str(e)


def test_calculation_read_schema():
    calc = CalculationRead(id=1, a=8, b=2, type="Divide", result=4)
    assert calc.id == 1
    assert calc.result == 4