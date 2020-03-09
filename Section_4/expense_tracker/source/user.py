class User:
	def __init__(self, user_name, email=None):
		self.name = user_name
		self.email = email
		self.expense_dict = {}

	def add_entry(self, user, amount):
		print(f"Now updating Entry {user.name} for {self.name}'s dict.")
		if self.expense_dict.get(user, None) is not None:
			print(f"Previous entry was {self.expense_dict[user]}")
			self.expense_dict[user] += amount
			print(f"New entry is {self.expense_dict[user]}")
		else:
			self.expense_dict[user] = amount
		

	def get_report(self):
		for user in self.expense_dict:
			amount = self.expense_dict[user]
			if amount < 0:
				print(f"{self.name} owes {user.name} {-1*amount} $")
			else:
				print(f"{self.name} has loaned {user.name} {amount} $")



