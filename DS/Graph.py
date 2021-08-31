class Vertex:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name


class Graph:
	vertices = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices.keys():
			self.vertices[vertex] = []
			return True
		else:
			return False

	def add_edge(self, u, v):
		if u in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.append(v)
				if key == v:
					value.append(u)
			return True
		else:
			return False

	def print_graph(self):
		print(self.vertices)


g = Graph()
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')

g.add_vertex(a)
g.add_vertex(b)


g.add_edge(a, b)
g.add_edge(a, c)
g.add_edge(a, d)

g.print_graph()
