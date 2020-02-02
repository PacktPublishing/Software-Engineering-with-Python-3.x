from source.calculator_with_stack import CalculatorStack
import pytest


@pytest.fixture
def calc_stack_int():
    my_obj = CalculatorStack()
    _ = my_obj.add_something(1, 3)
    _ = my_obj.add_something(4)
    # Stack value is 8
    return my_obj


@pytest.mark.parametrize("obj1, obj2, output",[
    (1, 2, 3),
    (10, -10, 0),
    (9, -8, 1),
    (1, None, 9),
    (10, 100, 110),
    (10, None, 18),
])
def test_add_something_int(calc_stack_int, obj1, obj2, output):
    assert calc_stack_int.add_something(obj1, obj2) == output
