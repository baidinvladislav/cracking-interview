from Graph import Graph, Vertex
from QueueStructure import Queue


def bfs(graph, s, t):
    """
    Implement of `Breath-First Search`.

    :param graph: adjacency list graph
    :param s: initial node
    :param t: destination node
    :return: True if destination node was reached
    """
    queue = Queue()
    queue.enqueue(s)
    s.visited = True

    while queue.is_empty is not True:
        v = queue.dequeue()
        for neighbor in graph.vertices[v]:
            if hasattr(neighbor, 'visited') is not True:
                queue.enqueue(neighbor)
                neighbor.visited = True
                if neighbor == t:
                    return True


g = Graph()
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')

g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)


g.add_edge(a, b)
g.add_edge(a, c)
g.add_edge(a, d)


bfs(g, a, d)
