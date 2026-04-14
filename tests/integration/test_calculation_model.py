from app.database import Base, engine, SessionLocal
from app.models.calculation import Calculation


Base.metadata.create_all(bind=engine)


def test_create_calculation_record():
    db = SessionLocal()

    calc = Calculation(a=10, b=5, type="Add", result=15)
    db.add(calc)
    db.commit()
    db.refresh(calc)

    saved_calc = db.query(Calculation).filter(Calculation.id == calc.id).first()

    assert saved_calc is not None
    assert saved_calc.a == 10
    assert saved_calc.b == 5
    assert saved_calc.type == "Add"
    assert saved_calc.result == 15

    db.delete(saved_calc)
    db.commit()
    db.close()
    