import csv
from collections import Counter
from .my_logger import logger


class ProcessData:
	"""This class processes the duplicated data.

	Methods
	-------
	read_data : read the duplicated data from csv file

	process_data : process the duplicated data from csv file

	Parameters
	----------
	file_name : name of csv file where emails are stored
	"""
	def __init__(self, file_name):
		self.data_file = file_name
		self.mails_list = []

	def read_data(self):
		"""Reads the csv file into a list of emails."""

		# Open CSV file
		with open(self.data_file, 'r') as f_data:

			# Use DictReader from csv module to read 
			# rows directly into a dictionary format
			csvreader = csv.DictReader(f_data) 
			
			# Iterate over the rows and add them to
			# the mails list
			for row in csvreader:
				self.mails_list.append(row)
			

	def process_data(self):
		"""Reads the csv file for emails and get counts of emails.

		This function reads the duplicated data from a csv file.
		Then using Counter from collections modules, it gets the 
		count of each unique entry.

		Returns
		-------
		mail_count : A dictionary with key as email entry and the 
			value as it's frequency.
		"""

		# Read the data from the csv
		self.read_data()

		# Use Counter from collections module
		# to get count of each unique email entry 
		mail_count = Counter(tuple(mail.values()) for mail in self.mails_list)
		
		logger.info(f'Count of unique emails is {mail_count}.')
		return mail_count

