from source.calculator import Calculator


def test_add_something_int():
    my_obj = Calculator()
    assert my_obj.add_something(1, 2) == 3
    assert my_obj.add_something(10, -10) == 0
    assert my_obj.add_something(-5, -5) == -10


def test_add_something_list():
    my_obj = Calculator()
    assert my_obj.add_something([1, 2, 3], [4]) == [1, 2, 3, 4]
    assert my_obj.add_something([1], [2]) == [1, 2]
    assert my_obj.add_something([1], []) == [1]


def test_add_something_str():
    my_obj = Calculator()
    assert my_obj.add_something('abc', '') == 'abc'
    assert my_obj.add_something('abc', 'd') == 'abcd'
    assert my_obj.add_something('abc', 'def') == 'abcdef'
