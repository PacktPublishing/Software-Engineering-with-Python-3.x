from source.calculator import Calculator
import pytest


@pytest.mark.parametrize("obj1, obj2, output",[
    (1, 2, 3),
    (10, -10, 0),
    (9, -8, 1),
    (10, 100, 110)
])
def test_add_something_int(obj1, obj2, output):
    my_obj = Calculator()
    assert my_obj.add_something(obj1, obj2) == output


@pytest.mark.parametrize("l1, l2, output_list", [
    ([1], [2], [1, 2]),
    ([1], [], [1]),
    ([1, 2, 3], [4, 5], [1, 2, 3, 4, 5]),
    ([1, 2], [3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
])
def test_add_something_list(l1, l2, output_list):
    my_obj = Calculator()
    assert my_obj.add_something(l1, l2) == output_list
