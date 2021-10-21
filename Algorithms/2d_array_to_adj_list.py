def build_graph(edges):
    """
    Returns adjacency list from edges list.

    :param edges: `List[List]` 2d array
    :return: `Dict[List]` adjacency list
    """
    graph = {}

    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph
