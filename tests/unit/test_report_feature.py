from app.schemas.report import CalculationStats


def test_calculation_stats_schema():
    stats = CalculationStats(
        total_calculations=10,
        total_add_operations=5,
        total_subtract_operations=2,
        highest_result=100,
        average_result=50
    )

    assert stats.total_calculations == 10
    assert stats.total_add_operations == 5
    assert stats.total_subtract_operations == 2
    assert stats.highest_result == 100
    assert stats.average_result == 50