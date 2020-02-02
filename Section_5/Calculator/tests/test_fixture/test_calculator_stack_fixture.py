from source.calculator_with_stack import CalculatorStack
import pytest


@pytest.fixture
def calc_stack_int():
    my_obj = CalculatorStack()
    _ = my_obj.add_something(1, 3)
    _ = my_obj.add_something(4)
    return my_obj


@pytest.fixture
def calc_stack_list():
    my_obj = CalculatorStack()
    _ = my_obj.add_something([1, 2], [3])
    _ = my_obj.add_something([4])
    return my_obj


def test_add_something_int_fixture(calc_stack_int):
    assert calc_stack_int.add_something(1) == 9
    assert calc_stack_int.add_something(-10) == -1
    assert calc_stack_int.add_something(-5, -5) == -10


def test_raised_exceptions_fixture(calc_stack_int):
    with pytest.raises(TypeError):
        assert calc_stack_int.add_something('abc', 1)


def test_add_something_list_fixture(calc_stack_list):
    assert calc_stack_list.add_something([1]) == [1, 4, 1, 2, 3]
    assert calc_stack_list.add_something([10], []) == [10]
    assert calc_stack_list.add_something([-5]) == [-5, 10]

