def some_function(nums):
	
	result = []
	even_string = 'Hello I am an even string!'
	odd_string = 'Hello I am an odd string!'

	for x in nums:
		if x%2==0:
			result.append((even_string, x))
		
		if x%5==0:
			result.append(("Hey! I am a multiple of Five", x))

		if x%2==1:
			result.append((odd_string, x))

	return result

def check_equal_length(nums, result):

	if len(nums)!=len(result):
		raise ValueError("More values in Result array!!")
	else:
		return True

def basic_operations():
	nums = list(range(10))

	result = some_function(nums)

	print("Recieved the values from function")

	for elem in result:
		print(elem)

	print("Now doing sanity check for equal length")
	
	if check_equal_length(nums, result) is True:
		print("All checks passed sucessfully!!")
	
if __name__ == "__main__":
	import pdb; pdb.set_trace()
	basic_operations()