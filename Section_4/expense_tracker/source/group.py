class UserGroup:
	def __init__(self, group_name, members):
		self.group_name = group_name
		self.members = members
		self.members_count = len(self.members)

	def update_group_expense(self, lender, amount):
		
		# Check if lender is in the group
		if lender in self.members:
			count_shares = self.members_count - 1
		else:
			count_shares = self.members_count

		for member in self.members:
			if lender == member:
				continue
			else:
				# Add owes entry
				member.add_entry(lender, -amount/count_shares)

				# Add loaned entry
				lender.add_entry(member, amount/count_shares)
