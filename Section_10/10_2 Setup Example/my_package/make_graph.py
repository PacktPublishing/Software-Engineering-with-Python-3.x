import networkx as nx
import pydot


class MakeGraphFile:
	"""This class is used to create a graph out of the list of
	emails.

	This class reads the duplicated list of emails, then creates a
	Directed Graph out of it, using NetworkX library. Finally, it 
	creates a .png file for the graph.

	Methods
	-------
	make_nx_graph : creates a NetworkX graph based on the list
		of emails
	
	write_dot_file : writes the Directed Graph to a dot file

	write_png_file : creates a .png file from the dot file

	Parameters
	----------
	mail_dicts : list of email dicts

	max_rep : max no. of times an email is to 
		duplicated(default: 10)
	"""
	def __init__(self, dot_file, png_file):
		"""Initialized the empty graph, dot file and png file name"""

		self.dot_file = dot_file
		self.png_file = png_file
		self.processed_graph = None

	def make_nx_graph(self, mails_data):
		"""Creates a Directed Graph based on email data.

		This function takes the duplicated emails list, then
		creates a Directed Graph out of them using NetworkX library.
		The weight of each edge is the number of times the value is
		duplicated.

		Parameters
		----------
		mails_data : list of email dicts
		"""

		# Create an empty directed graph
		self.processed_graph = nx.DiGraph()

		for mail in mails_data:
			# Each 'mail' is a key, of type tuple
			# Each key if of the form (source, destination)
			source = mail[0]
			destination = mail[1]

			# Use the key to get the count
			mail_count = mails_data[mail]

			# Add edges to the graph
			self.processed_graph.add_edge(source,
									destination,
									label=mail_count)

	def write_dot_file(self, mails_data):
		"""Creates a Graph from the list of emails, then writes the
		NetworkX graph to a dot file.

		Parameters
		----------
		mails_data: list of email dicts

		"""
		self.make_nx_graph(mails_data)
		nx.drawing.nx_pydot.write_dot(self.processed_graph,
									self.dot_file)

	def write_png_file(self):
		"""Create a .png file from the dot file saved previously."""

		# Read the graph from the dot file
		(graph,) = pydot.graph_from_dot_file(self.dot_file)

		# Write the dot file to a png
		graph.write_png(self.png_file)