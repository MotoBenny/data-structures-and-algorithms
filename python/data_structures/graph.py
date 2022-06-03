class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """
        add node
        Arguments: value
        Returns: The added node
        Add a node to the graph
        """
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def size(self):
        return len(self._adjacency_list)

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def add_edge(self, start_vertex, end_vertex, weight: int = 0):
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError()

        edge = Edge(end_vertex, weight)

        self._adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        return self._adjacency_list.keys()


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight: int):
        self.vertex = vertex
        self.weight = weight
