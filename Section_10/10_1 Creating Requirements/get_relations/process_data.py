import csv
from collections import Counter


class ProcessData:
	def __init__(self, file_name):
		self.data_file = file_name
		self.mails_list = []

	def read_data(self):

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

		# Read the data from the csv
		self.read_data()

		# Use Counter from collections module
		# to get count of each unique email entry 
		mail_count = Counter(tuple(mail.values()) for mail in self.mails_list)
		
		return mail_count

