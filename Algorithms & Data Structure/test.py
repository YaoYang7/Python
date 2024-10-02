class Graph1:
    def __init__(self):
        self._AdjacencyMap = {}

    def vertices(self):
        return self._AdjacencyMap.keys()

class Graph2:
    def __init__(self):
        self._Adjacency_Map = {}

    def vertices(self):
        return [str(vertex) for vertex in self._Adjacency_Map.keys()]

# Example usage
graph1 = Graph1()
graph1._AdjacencyMap = {'A': {}, 'B': {}, 'C': {}}

graph2 = Graph2()
graph2._Adjacency_Map = {'1': {}, '2': {}, '3': {}}

print("Vertices of graph1:")
print(graph1.vertices())  # Directly returns keys

print("\nVertices of graph2:")
print(graph2.vertices())  # Converts keys to strings before returning
