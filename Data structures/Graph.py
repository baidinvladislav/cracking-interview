class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()

	def add_neighbor(self, v):
		if v in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()


class Graph:
	pass
