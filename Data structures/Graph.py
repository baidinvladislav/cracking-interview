class Vertex:
	def __init__(self, name):
		self.name = name
		self.neighbors = list()

	def add_neighbor(self, v):
		if v.name not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()


class Graph:
	vertices = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False

	def add_edge(self, u, v):
		if u.name in self.vertices and v.name in self.vertices:
			for key, value in self.vertices.items():
				if key == u.name:
					value.add_neighbor(v)
				if key == v.name:
					value.add_neighbor(u)
			return True
		else:
			return False

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))


g = Graph()
a = Vertex('A')
b = Vertex('B')

g.add_vertex(a)
g.add_vertex(b)

g.add_edge(a, b)

print(g.vertices)
