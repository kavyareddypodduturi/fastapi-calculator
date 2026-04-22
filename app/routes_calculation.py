from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate, CalculationRead

router = APIRouter(prefix="/calculations", tags=["Calculations"])


@router.post("", response_model=CalculationRead)
def create_calculation(calculation: CalculationCreate, db: Session = Depends(get_db)):
    if calculation.type == "Add":
        result = calculation.a + calculation.b
    elif calculation.type == "Sub":
        result = calculation.a - calculation.b
    elif calculation.type == "Multiply":
        result = calculation.a * calculation.b
    elif calculation.type == "Divide":
        result = calculation.a / calculation.b

    new_calculation = Calculation(
        a=calculation.a,
        b=calculation.b,
        type=calculation.type,
        result=result
    )

    db.add(new_calculation)
    db.commit()
    db.refresh(new_calculation)
    return new_calculation


@router.get("", response_model=list[CalculationRead])
def get_calculations(db: Session = Depends(get_db)):
    calculations = db.query(Calculation).all()
    return calculations


@router.get("/{calculation_id}", response_model=CalculationRead)
def get_calculation(calculation_id: int, db: Session = Depends(get_db)):
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()

    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")

    return calculation

@router.put("/{calculation_id}", response_model=CalculationRead)
def update_calculation(calculation_id: int, updated: CalculationCreate, db: Session = Depends(get_db)):
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()

    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")

    # recalculate result
    if updated.type == "Add":
        result = updated.a + updated.b
    elif updated.type == "Sub":
        result = updated.a - updated.b
    elif updated.type == "Multiply":
        result = updated.a * updated.b
    elif updated.type == "Divide":
        result = updated.a / updated.b

    calculation.a = updated.a
    calculation.b = updated.b
    calculation.type = updated.type
    calculation.result = result

    db.commit()
    db.refresh(calculation)

    return calculation

@router.delete("/{calculation_id}")
def delete_calculation(calculation_id: int, db: Session = Depends(get_db)):
    calculation = db.query(Calculation).filter(Calculation.id == calculation_id).first()

    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")

    db.delete(calculation)
    db.commit()

    return {"message": "Calculation deleted successfully"}