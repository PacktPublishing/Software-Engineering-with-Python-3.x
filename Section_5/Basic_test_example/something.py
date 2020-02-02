def add_something(my_list, my_int):
	if my_int is None:
		return my_list

	for idx, elem in enumerate(my_list):
		if type(elem) is not int:
			return None
		else:
			my_list[idx] = elem + my_int
			
	return my_list

print(add_something([1, 2, 3], 10))
print(add_something([1, 'abc', 3], 10))
print(add_something([1, 2, 3, 4], None))