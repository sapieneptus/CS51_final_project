class word_node(object):
	def __init__(self, word):
		self.word 			= word
		self.connections 	= {}

	def connect(self, connection):
		if connection not in self.connections:
			self.connections[connection] = True

	def disconnect(self, connection):
		if connection in self.connections:
			del self.connections[connection]

class node_connection(object):
	"""
		A node connection is a connection from one node
		to another. Since connections are directed,
		they should be associated with a starting node 
		and contain information about the destination node
		as well as the type of connection. 

		If I were being proscriptive, the connection types
		would be some extension of the set:
		
		{[ "has_a", "is_a", "belongs_to_a", "does", "is_done_by", ... ]}

		However, ideally the agent will learn to generate it's own
		connection types and realize that "dog" and "tail" have
		the same connection type as "cat" and "tail". 

	"""
	def __init__(self, node, con_type):
		self.node 	= node
		self.type 	= con_type 


class semantic_graph(object):
	def __init__(self, nodes):
		self.nodes = nodes

	def semantically_similar(self, node, other_node):
		"""
			Need to determine how to codify the notion of semantically
			similarity...
		"""
		pass 