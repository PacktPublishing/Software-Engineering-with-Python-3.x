def do_something():

	import pdb; pdb.set_trace()
	
	first_var = 1

	print("Initialized Variable No. {}".format(first_var))

	second_var = 2

	print("Initialized Variable No. {}".format(second_var))

	third_var = 3

	print("Initialized Variable No. {}".format(third_var))

	fourth_var = 4

	print("Initialized Variable No. {}".format(fourth_var))

	fifth_var = 5

	print("Initialized Variable No. {}".format(fifth_var))

	print("Calling Other Function")

	other_function()

	print("End of do_something")

	return "End of Function No. 1"

def other_function():

	sixth_var = 6

	print("Initialized Variable No. {}".format(sixth_var))

	seventh_var = 7

	print("Initialized Variable No. {}".format(seventh_var))

	eigth_var = 8

	print("Initialized Variable No. {}".format(eigth_var))

	ninth_var = 9

	print("Initialized Variable No. {}".format(ninth_var))

	tenth_var = 10

	print("Initialized Variable No. {}".format(tenth_var))

	final_function()

	print("End of other_function")

	return "End of Function No. 2"

def final_function():

	eleventh_var = 11

	print("Initialized Variable No. {}".format(eleventh_var))

	twelth_var = 12

	print("Initialized Variable No. {}".format(twelth_var))

	thirteenth_var = 13

	print("Initialized Variable No. {}".format(thirteenth_var))

	print("End of final_function")

	return "End of Function No. 3"

do_something()