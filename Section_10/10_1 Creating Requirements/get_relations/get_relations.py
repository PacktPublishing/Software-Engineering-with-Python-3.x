from make_graph import MakeGraphFile
from process_data import ProcessData
from data_dict import DataDict


class EmailRelations:

	def __init__(self, data_dicts, max_rep, csv_fname, dot_fname, png_fname):
		self.data_dicts = data_dicts
		self.max_rep = max_rep
		self.csv_file_name = csv_fname
		self.dot_file_name = dot_fname
		self.png_file_name = png_fname

	def create_relations_image(self):
		# Create the random data
		data_dict_obj = DataDict(self.data_dicts, self.max_rep)

		# Write the data to a csv file
		data_dict_obj.write_dup_data(self.csv_file_name)

		# Process the data and get counts of emails
		process_data_obj = ProcessData(self.csv_file_name)
		processed_counts = process_data_obj.process_data()

		# Make a graph of the processed data
		graph_file_obj = MakeGraphFile(self.dot_file_name, self.png_file_name)
		graph_file_obj.write_dot_file(processed_counts)

		# Write the graph to a file
		graph_file_obj.write_png_file()
