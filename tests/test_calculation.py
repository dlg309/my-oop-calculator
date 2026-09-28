from calculator.calculation import Add

def test_add():
    calculation = Add(10, 5)
    result = calculation.get_result()
    assert result == 15