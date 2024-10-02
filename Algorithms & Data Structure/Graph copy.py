
class Vertex() :
    def __init__(self, element):
        self._element = element

    def __str__(self):
        return str(self._element)

class Edge():
    def __init__(self, v1, v2, weight):
        self._edge = (f"Edge: {v1}{v2}") # edge table 
        self._weight = weight
        self._v1 = v1 # start
        self._v2 = v2 # end
    
    def __str__(self):
        return f"Edge: {self._v1} <--> {self._v2} | Weight: {self._weight}"
    
    def opposite(self, vertex):
        if vertex == self._v1:
            return self._v2 # vertex is v1, so opposite is v2
        else:
            return self._v1 # vertex isn't v1, so it's v2 and opposite of v2 is v1
        
    def element(self):
        return self._edge # return the label of edge

class Graph():
    def __init__(self):
        self = {} # each vertex(Key) maintains (value) a hash-map where the other vertices
                                # are the keys and the incident edges are teh values
        
    def __str__(self):
        string = ""
        for vertex in self._AdjacencyMap:
            for connectedVertex, edge in self._AdjacencyMap[vertex].items():
                string += str(vertex) + str(connectedVertex) + " | " + str(edge) + "\n"
            string += "\n"
        return string
    
    def vertices(self):
        # return self._AdjacencyMap.keys() # returns "dict_keys(['A', 'B', 'C'])"
        return [str(vertex) for vertex in self._AdjacencyMap.keys()] # returns "['A', 'B', 'C']" 
    
    def edges(self):
        edges = set() # stores only unique values, avoids dupes 
        for vertex in self._Adjacency_Map:
            for edge in self._Adjacency_Map[vertex]:
                edges.add(str(self._Adjacency_Map[vertex][edge]))
        return list(edges)
    
    def num_vertices(self):
        return len(self.vertices()) # returns the number of vertices
    
    def num_edges(self):
        return len(self.edges()) # returns the number of edges
    
    def get_edge(self, v1, v2):
        if v1 in self._AdjacencyMap and v2 in self._AdjacencyMap[v1]:
            return self._AdjacencyMap[v1][v2] # returns the edge between v1 and v2
        else:
            return None # returns None if there is no edge between v1 and v2
        
    def degree(self, vertex):
        return len(self._AdjacencyMap[vertex]) # returns the number of edges incident to the vertex
    
    def get_edges(self, vertex):
        return [edge for edge in self._Adjacency_Map[vertex].values()] # returns the edges incident to the vertex
    
    def add_vertex(self, element):
        for v in self._AdjacencyMap:
            if v._element == element:
                return v
            
        new_v = Vertex(element)
        self._AdjacencyMap[new_v] = dict()
        return new_v
    
    def add_edge(self, v1, v2, weight): 
        if v1 and v2 in self._AdjacencyMap:
            new_edge = Edge(v1, v2, weight)
            self._AdjacencyMap[v1][v2] = new_edge
            self._AdjacencyMap[v2][v1] = new_edge
            return new_edge
        
    def remove_vertex(self, vertex):
        v = vertex
        if v in self._AdjacencyMap:
            for connectedV in self._AdjacencyMap[v]:
                self._AdjacencyMap[connectedV].pop(v)
            self._AdjacencyMap.pop(v)
        else:
            print("Vertex not found")
            
    def remove_edge(self, edge): 
        e = edge 
        v1 = e._v1
        v2 = e._v2

        if (v1 in self._Adjacency_Map and v2 in self._Adjacency_Map[v1]) and (v2 in self._Adjacency_Map and v1 in self._Adjacency_Map[v2]):
            self._AdjacencyMap[v1].pop(v2)
            self._AdjacencyMap[v2].pop(v1)
        else:
            print("Edge not found")

def PrimAQP

def PrimUL

if __name__ == "__main__":
    import random
    import time
    import heapq
    # creating a random graph
    def generateGraph(n, m): # n = number of vertices, m = number of edges
        graph = Graph()
        vertices = []

        for i in range(n):
            v = graph.add_vertex("Vertex" + str(i)) # add vertex to graph, Vertex1 to Vertexn-1
            vertices.append(v)

        # line 117 to 127 is taken off chatGPT 
        connected = []
        for v in vertices:
            connected.append(v)
            if len(connected) != 1:
                v2 = random.choice(connected)
                while v == v2:
                    v2 = random.choice(connected)
                graph.add_edge(v, v2, weight = random.randint(1, 20))
        max_edges = n*(n-1)
        more_edges = int(round((max_edges*m), ) - (n-1))

        for _ in range(more_edges):
            # Chose 2 different vertices at random from the list 
            v1 = random.choice(vertices)
            v2 = random.choice(vertices)
            # Ensure the selected vertices are different and have different edges and not already in graph
            while v1 == v2 or graph.get_edge(v1, v2) is not None:
                v1 = random.choice(vertices)
                v2 = random.choice(vertices)
    
            # checking if an edge exists in the graph, if it doesn't exist then we can add it to our graph
            if graph.get_edge(v1, v2) is None:
                graph.add_edge(v1, v2, weight = random.randint(1, 20))
        return graph
