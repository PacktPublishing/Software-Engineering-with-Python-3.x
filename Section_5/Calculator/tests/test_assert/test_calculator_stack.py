from source.calculator_with_stack import CalculatorStack
import pytest


def test_add_something_stack_int():
    my_obj = CalculatorStack()
    _ = my_obj.add_something(1, 3)
    _ = my_obj.add_something(4)
    assert my_obj.add_something(1) == 9
    assert my_obj.add_something(-10) == -1
    assert my_obj.add_something(-5, -5) == -10


@pytest.mark.xyz
def test_stack_raised_exceptions():
    my_obj = CalculatorStack()
    _ = my_obj.add_something(1, 3)
    _ = my_obj.add_something(4)
    with pytest.raises(TypeError):
        assert my_obj.add_something('abc', 1)



