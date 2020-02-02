def some_function(nums):
	
	result = []
	even_string = 'Hello I am an even string!'
	odd_string = 'Hello I am an odd string!'

	for x in nums:
		if x%2==0:
			result.append(even_string)
		
		if x%5:
			result.append("Hey! I am a multiple of Five")

		if x%2==1:
			result.append(odd_string)

	return result

def basic_operations():
	nums = list(range(10))

	result = some_function(nums)

	if len(result)!=len(nums):
		raise ValueError("More values in Result array!!")

basic_operations()