class Expense:
	def __init__(self, lender, amount, lendee=None, group=None):
		self.lender = lender
		self.lendee = lendee
		self.group = group
		self.amount = amount

		if isinstance(self.lendee, list) or self.group is not None:
			self.transaction_type = 'multiple'
		else:
			self.transaction_type = 'single'
		self.update_expenses()

	def update_expenses(self):
		# Check if the amount is loaned to a Group
		if self.group is None:
			self.update_user_expenses()
		else:
			self.group.update_group_expense(self.lender, self.amount)

	def update_user_expenses(self):

		if self.transaction_type == 'single':
			print("Updating single non-group expense")
			self.lender.add_entry(self.lendee, self.amount)
			self.lendee.add_entry(self.lender, -self.amount)
		else:
			print("Updating multiple non-group expenses")
			lendees_count = len(self.lendee)
			print(f"Lendees are {lendees_count}")
			for lendee in self.lendee:
				self.lender.add_entry(lendee, self.amount/lendees_count)
				lendee.add_entry(self.lender, -self.amount/lendees_count)
