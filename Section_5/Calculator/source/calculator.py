class Calculator:
	def __init__(self):
		pass

	def check_types(self, obj1, obj2):
		if type(obj1) == type(obj2):
			return True
		else:
			print("Incompatible arg types")
			raise TypeError

	def add_something(self, obj1, obj2):
		if self.check_types(obj1, obj2):
			
			result = None

			try:
				result = obj1 + obj2
			except TypeError as err:
				print("TypeError occured while adding args")
				print(err)
			finally:
				return result

		else:
			return None

	def sub_something(self, obj1, obj2):
		if self.check_types(obj1, obj2):
			result = None

			try:
				result = obj1 - obj2
			except TypeError as err:
				print("TypeError occured while subtracting args")
				print(err)
			finally:
				return result
		else:
			return None

	def mul_something(self, obj1, obj2):
		if self.check_types(obj1, obj2):
			result = None

			try:
				result = obj1 * obj2
			except TypeError as err:
				print("TypeError occured while multiplying args")
				print(err)
			finally:
				return result
		else:
			return None

	def div_something(self, obj1, obj2):
		if self.check_types(obj1, obj2):
			result = None

			try:
				result = obj1 / obj2
			except TypeError as err:
				print("TypeError occured while multiplying args")
				print(err)
			except ZeroDivisionError as err:
				print("You tried to divide by Zero")
			finally:
				return result
		else:
			return None


