class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.graph = {}

    def add_node(self, vertex):
        self.graph[vertex] = Vertex(vertex)
        return self.graph[vertex]

    def add_edge(self, vertex_1, vertex_2, value):
        vertex_1.add_edge(vertex_2, value)
        vertex_2.add_edge(vertex_1, value)

    def get_vertices(self):
        return self.graph.values()

    def get_neighbors(self, vertex):
        return vertex.values()

    def size(self):
        return len(self.graph)


class Vertex:
    def __init__(self, value):
        self.neighbors = {}
        self.value = value

    def add_edge(self, vertex, edge):
        self.neighbors[vertex] = edge

    def values(self):
        return list(self.neighbors.keys())

