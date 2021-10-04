class DisjointSets:

    def __init__(self, vertex_array):
        """
        Creates the array where index is vertex and value is a root vertex.

        :param vertex_array: list contains all vertexes.
        """
        self.vertexes = list(range(len(vertex_array)))

    def find(self, v):
        """
        Returns the root of the vertex, if the vertex is not a root for itself,
        then recursively searches for its root.

        :param v: vertex whose root vertex we find.
        :return: root of vertex represented value in `self.vertexes` array.
        """
        if v != self.vertexes[v]:
            self.find(self.vertexes[v])
        return self.vertexes[v]

    def union(self, v, u):
        """
        Unions two received vertexes.

        :param v: first vertex to union
        :param u: second vertex to union
        :return: `True` if union went successfully and `False` if did not.
        """
        v_root = self.find(v)
        u_root = self.find(u)

        if v_root != u_root:
            self.vertexes[u] = self.vertexes[v]
            return True

        return False
