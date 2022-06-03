import instantiate as instantiate


class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        """
        we create a property to hold our Graphs dictionary, our adjacency list
        """
        self._adjacency_list = {}

    def add_node(self, value):
        """
        create a vertex variable calling the Vertex class, with tha value as argument.
        We then add that value as a key in our dictionary with that keys value being our empyty list.
        and return the vertex
        """
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def size(self):
        """
        we simply check the size of our adjacency list dictionary and return that.
        """
        return len(self._adjacency_list)

    def get_neighbors(self, vertex):
        """
        we call our adjacency list with the vertex arg as the key, this returns the value list at that key.
        """
        return self._adjacency_list[vertex]

    def add_edge(self, start_vertex, end_vertex, weight: int = 0):
        """
        If the start or end vertex is not in our dict, we cant connect them, raise key error.
        otherwise we instantiate an instance of our Edge class, with the end vertex and the weight
        we then use our start vertex as a key and append the new edge to the key in our adjacency dictionary
        """
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError()

        edge = Edge(end_vertex, weight)

        self._adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
        simply returns the keys from our adjacency dictionary
        """
        return self._adjacency_list.keys()


class Vertex:
    """
    Vertex or node Simply holds the value, and needs no other properties.
    """
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight: int):
        self.vertex = vertex
        self.weight = weight
