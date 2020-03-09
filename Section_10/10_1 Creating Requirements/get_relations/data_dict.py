import csv
import random


class DataDict:
	def __init__(self, mail_dicts, max_rep=10):
		self.mail_dict_list = mail_dicts
		self.max_rep = max_rep
		self.duplicated_dict_list = []

	def duplicate_data(self):

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

		# Duplicate the entries of the email dict
		self.duplicate_data()

		# Get the keys, i.e. 'From' and 'To'
		# This will be used to write the header of csv
		key_list = self.mail_dict_list[0].keys()

		# Write the data to the csv file
		with open('mails.csv', 'w') as f_data:
			csv_writer = csv.DictWriter(f_data, key_list)
			csv_writer.writeheader()
			csv_writer.writerows(self.duplicated_dict_list)