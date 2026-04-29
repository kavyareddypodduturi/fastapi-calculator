from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate, CalculationUpdate, CalculationRead

router = APIRouter(prefix="/calculations", tags=["Calculations"])


# TEMP user
def get_current_user_id():
    return 1


# BROWSE
@router.get("/")
def browse_calculations(db: Session = Depends(get_db)):
    user_id = get_current_user_id()
    return db.query(Calculation).filter(Calculation.user_id == user_id).all()


# READ
@router.get("/{calculation_id}")
def read_calculation(calculation_id: int, db: Session = Depends(get_db)):
    user_id = get_current_user_id()

    calc = db.query(Calculation).filter(
        Calculation.id == calculation_id,
        Calculation.user_id == user_id
    ).first()

    if not calc:
        raise HTTPException(status_code=404, detail="Not found")

    return calc


# ADD
@router.post("/", response_model=CalculationRead)
def add_calculation(data: CalculationCreate, db: Session = Depends(get_db)):
    user_id = get_current_user_id()

    if data.type == "Add":
        result = data.a + data.b
    elif data.type == "Sub":
        result = data.a - data.b
    elif data.type == "Multiply":
        result = data.a * data.b
    elif data.type == "Divide":
        if data.b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = data.a / data.b
    else:
        raise HTTPException(status_code=400, detail="Invalid type")

    new_calc = Calculation(
        a=data.a,
        b=data.b,
        type=data.type,
        result=result,
        user_id=user_id
    )

    db.add(new_calc)
    db.commit()
    db.refresh(new_calc)

    return new_calc


# EDIT
@router.put("/{calculation_id}")
def edit_calculation(calculation_id: int, data: CalculationUpdate, db: Session = Depends(get_db)):
    user_id = get_current_user_id()

    calc = db.query(Calculation).filter(
        Calculation.id == calculation_id,
        Calculation.user_id == user_id
    ).first()

    if not calc:
        raise HTTPException(status_code=404, detail="Not found")

    if data.a is not None:
        calc.a = data.a
    if data.b is not None:
        calc.b = data.b
    if data.type is not None:
        calc.type = data.type

    # recalculate result
    if calc.type == "Add":
        calc.result = calc.a + calc.b
    elif calc.type == "Sub":
        calc.result = calc.a - calc.b
    elif calc.type == "Multiply":
        calc.result = calc.a * calc.b
    elif calc.type == "Divide":
        if calc.b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        calc.result = calc.a / calc.b

    db.commit()
    db.refresh(calc)

    return calc


# DELETE
@router.delete("/{calculation_id}")
def delete_calculation(calculation_id: int, db: Session = Depends(get_db)):
    user_id = get_current_user_id()

    calc = db.query(Calculation).filter(
        Calculation.id == calculation_id,
        Calculation.user_id == user_id
    ).first()

    if not calc:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(calc)
    db.commit()

    return {"message": "Calculation deleted successfully"}