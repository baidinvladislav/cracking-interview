from Graph import Graph, Vertex


def dfs(graph, v, t):
    """
    Implement of `Depth-First Search`.

    :param graph: adjacency list graph
    :param v: visited node
    :param t: destination node
    :return: True if destination node was reached
    """
    if v == t:
        return True

    if hasattr(v, 'visited'):
        return True

    v.visited = True
    for neighbor in graph.vertices[v]:
        if hasattr(neighbor, 'visited') is not True:
            reached = dfs(graph, neighbor, t)
            if reached:
                print(f'We have reached the destination node')
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


dfs(g, a, d)
