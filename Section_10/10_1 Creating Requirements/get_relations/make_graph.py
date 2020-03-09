import networkx as nx
import pydot


class MakeGraphFile:
	def __init__(self, dot_file, png_file):
		self.dot_file = dot_file
		self.png_file = png_file
		self.processed_graph = None

	def make_nx_graph(self, mails_data):

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
		self.make_nx_graph(mails_data)
		nx.drawing.nx_pydot.write_dot(self.processed_graph,
									self.dot_file)

	def write_png_file(self):

		# Read the graph from the dot file
		(graph,) = pydot.graph_from_dot_file(self.dot_file)

		# Write the dot file to a png
		graph.write_png(self.png_file)