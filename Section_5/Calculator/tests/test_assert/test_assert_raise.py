from source.calculator import Calculator
import pytest


@pytest.mark.xyz
def test_add_something_raise():
    my_obj = Calculator()
    with pytest.raises(TypeError):
        assert my_obj.add_something(1, 'abc')


def test_mul_something_list():
    my_obj = Calculator()
    assert my_obj.mul_something([1, 2, 3], [4, 5]) is None
