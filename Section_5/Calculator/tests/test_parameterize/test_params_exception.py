import pytest
from source.calculator_with_stack import CalculatorStack


@pytest.fixture
def calc_stack_int():
    my_obj = CalculatorStack()
    _ = my_obj.add_something(1, 3)
    _ = my_obj.add_something(4)
    return my_obj


@pytest.mark.parametrize("obj1, obj2, exception",[
    (5, 'abc', pytest.raises(TypeError)),
    ({1: 100}, None, pytest.raises(NotImplementedError)),
    (set([1, 2]), set([3, 4]), pytest.raises(NotImplementedError))
])
def test_params_exception(calc_stack_int, obj1, obj2, exception):
    with exception:
        assert calc_stack_int.add_something(obj1, obj2) is not None