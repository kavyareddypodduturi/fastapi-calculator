from pydantic import BaseModel, field_validator, model_validator


class CalculationCreate(BaseModel):
    a: float
    b: float
    type: str

    @field_validator("type")
    @classmethod
    def validate_type(cls, value):
        allowed_types = ["Add", "Sub", "Multiply", "Divide"]
        if value not in allowed_types:
            raise ValueError("type must be Add, Sub, Multiply, or Divide")
        return value

    @model_validator(mode="after")
    def validate_divide_by_zero(self):
        if self.type == "Divide" and self.b == 0:
            raise ValueError("Division by zero is not allowed")
        return self


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: str
    result: float | None = None

    class Config:
        from_attributes = True