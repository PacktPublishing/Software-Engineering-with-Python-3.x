from Basic_test_example.something import add_something

def test_add_int():
	assert add_something([1, 2, 3], 10) == [11, 12, 13]

def test_add_int_None():
	assert add_something([1, 2], None) == [1, 2]

def test_add_int_invalid_list():
	assert add_something([1, 'abc'], 10) == None
	assert add_something([1, {1: 100}], 10) == None