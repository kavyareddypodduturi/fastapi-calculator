from pydantic import BaseModel


class CalculationStats(BaseModel):
    total_calculations: int
    total_add_operations: int
    total_subtract_operations: int
    highest_result: float | None
    average_result: float | None