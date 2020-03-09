import csv
import random


class DataDict:
	"""This class takes a list of emails & duplicates them 
	and then writes the duplicated data to a csv file.

	Methods
	-------
	duplicate_data : duplicates the list of emails randomly
	
	write_dup_data : writes the duplicated data to a csv file

	Parameters
	----------
	mail_dicts : list of email dicts

	max_rep : max no. of times an email is to 
		duplicated(default: 10)
	"""
	def __init__(self, mail_dicts, max_rep=10):
		"""Initialize the list of email dicts, max. repitions and
		duplicated_list.
		
		Parameters
		----------
		mail_dicts : list of email dicts

		max_rep : maximum no. of times an email is to
			duplicated(default: 10)
		"""
		self.mail_dict_list = mail_dicts
		self.max_rep = max_rep
		self.duplicated_dict_list = []

	def duplicate_data(self):
		""" Duplicates the list of emails.

		This function randomly duplicates each entry in the list of
		emails. Then adds them to duplicated_dict_list, followed by
		shuffling it.
		"""

		# Get an entry from the email dictionary
		for mail in self.mail_dict_list:

			# Choose a random number from 2 to max_rep
			times = random.randrange(2, self.max_rep)

			# Duplicate that entry based on the random
			# number generated above
			for x in range(0, int(times)):
				self.duplicated_dict_list.append(mail)

		# Shuffle the data
		random.shuffle(self.duplicated_dict_list)

	def write_dup_data(self, file_name):
		"""This function writes the duplicated data to a csv file.

		Parameters
		----------
		file_name: csv file name where the duplicated data is to be saved.
		"""

		# Duplicate the entries of the email dict
		self.duplicate_data()

		# Get the keys, i.e. 'From' and 'To'
		# This will be used to write the header of csv
		key_list = self.mail_dict_list[0].keys()

		# Write the data to the csv file
		with open(file_name, 'w') as f_data:
			csv_writer = csv.DictWriter(f_data, key_list)
			csv_writer.writeheader()
			csv_writer.writerows(self.duplicated_dict_list)