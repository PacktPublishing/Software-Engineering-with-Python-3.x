def simple_function():

	some_var = "Hello! I am a string!"

	x = 5

	nums = list(range(10))

	y = "My value is {}".format(x + 1)

	nums[2] = y

	print(nums)

	return nums

if __name__ == "__main__":
	import pdb; pdb.set_trace()
	result = simple_function()
	print("Done Executing Simple Function")
	print("The returned value is ", result)
	print("This is the end of program!")