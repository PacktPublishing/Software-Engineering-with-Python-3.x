from source.custom_exception import StackEmpty


class CalculatorStack:
	def __init__(self):
		self.stack = []

	def check_stack(self):
		if not self.stack:
			raise StackEmpty
		else:
			return True

	def check_types(self, obj1, obj2):
		if type(obj1) is dict or type(obj1) is set:
			raise NotImplementedError

		if type(obj1) == type(obj2):
			return True
		else:
			print("Incompatible arg types")
			raise TypeError

	def add_something(self, obj1, obj2=None):
		if obj2 is None:
			# 1. Check if stack has value
			# 2. Check if top of stack is of same type as obj1
			if self.check_stack():
				if self.check_types(obj1, self.stack[-1]):
					obj2 = self.stack.pop()
			else:
				return None

		if self.check_types(obj1, obj2):
			
			result = None

			try:
				result = obj1 + obj2
				self.stack.append(result)
			except TypeError as err:
				print("TypeError occured while adding args")
				print(err)
			finally:
				return result

		else:
			return None
