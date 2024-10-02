import random

class Vertex:
    def __init__(self, element):
        self._element = element

    def __str__(self):
        return str(self._element)

class Edge:
    def __init__(self, v1, v2, weight):
        self._edge = f"Edge: {v1}{v2}"  # edge table
        self._weight = weight
        self._v1 = v1  # start
        self._v2 = v2  # end

    def __str__(self):
        return f"Edge: {self._v1} <--> {self._v2} | Weight: {self._weight}"

    def opposite(self, vertex):
        if vertex == self._v1:
            return self._v2  # vertex is v1, so opposite is v2
        else:
            return self._v1  # vertex isn't v1, so it's v2 and opposite of v2 is v1

    def element(self):
        return self._edge  # return the label of edge

class Graph:
    def __init__(self):
        self._adjacency_map = {}  # Store the graph structure

    def __str__(self):
        string = ""
        for vertex in self._adjacency_map:
            for connected_vertex, edge in self._adjacency_map[vertex].items():
                string += str(vertex) + str(connected_vertex) + " | " + str(edge) + "\n"
            string += "\n"
        return string

    def vertices(self):
        return [str(vertex) for vertex in self._adjacency_map.keys()]

    def edges(self):
        edges = set()
        for vertex in self._adjacency_map:
            for edge in self._adjacency_map[vertex].values():
                edges.add(str(edge))
        return list(edges)

    def num_vertices(self):
        return len(self._adjacency_map)

    def num_edges(self):
        return sum(len(edges) for edges in self._adjacency_map.values()) // 2

    def get_edge(self, v1, v2):
        if v1 in self._adjacency_map and v2 in self._adjacency_map[v1]:
            return self._adjacency_map[v1][v2]
        else:
            return None

    def degree(self, vertex):
        return len(self._adjacency_map[vertex])

    def get_edges(self, vertex):
        return list(self._adjacency_map[vertex].values())

    def add_vertex(self, element):
        new_vertex = Vertex(element)
        self._adjacency_map[new_vertex] = {}
        return new_vertex

    def add_edge(self, v1, v2, weight):
        if v1 in self._adjacency_map and v2 in self._adjacency_map:
            new_edge = Edge(v1, v2, weight)
            self._adjacency_map[v1][v2] = new_edge
            self._adjacency_map[v2][v1] = new_edge
            return new_edge

    def remove_vertex(self, vertex):
        if vertex in self._adjacency_map:
            for connected_vertex in self._adjacency_map[vertex]:
                self._adjacency_map[connected_vertex].pop(vertex)
            del self._adjacency_map[vertex]
        else:
            print("Vertex not found")

    def remove_edge(self, edge):
        v1 = edge._v1
        v2 = edge._v2

        if v1 in self._adjacency_map and v2 in self._adjacency_map[v1]:
            del self._adjacency_map[v1][v2]
            del self._adjacency_map[v2][v1]
        else:
            print("Edge not found")

def PrimAPQ(graph):
    marked = set()
    mst = []
    pq = []
    locs = {}
    start_vertex = next(iter(graph.vertices()))

    def visit(vertex):
        marked.add(vertex)
        for edge in graph.get_edges(vertex):
            opposite_vertex = edge.opposite(vertex)
            if opposite_vertex not in marked:
                heapq.heappush(pq, (edge._weight, (vertex, edge)))

    visit(start_vertex)
    while pq:
        c, (v, e) = heapq.heappop(pq)
        if v not in locs:
            mst.append(e) if e else None
            locs[v] = True
            visit(v)
    return mst

def PrimUL(graph):
    marked = set()
    mst = []
    start_vertex = next(iter(graph.vertices()))

    def visit(vertex):
        marked.add(vertex)
        for edge in graph.get_edges(vertex):
            opposite_vertex = edge.opposite(vertex)
            if opposite_vertex not in marked:
                mst.append(edge)

    visit(start_vertex)
    while len(mst) < graph.num_vertices() - 1:
        min_edge = None
        min_weight = float('inf')
        for vertex in marked:
            for edge in graph.get_edges(vertex):
                if edge.opposite(vertex) not in marked and edge._weight < min_weight:
                    min_edge = edge
                    min_weight = edge._weight
        if min_edge:
            visit(min_edge.opposite(min_edge._v1))
    return mst

def generateGraph(n, m): # n = number of vertices, m = number of edges
    graph = Graph()
    vertices = []

    for i in range(n):
        v = graph.add_vertex("Vertex" + str(i)) # add vertex to graph, Vertex1 to Vertexn-1
        vertices.append(v)

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
        # Choose 2 different vertices at random from the list 
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

if __name__ == "__main__":
    n = 6  # Number of vertices
    m = 0.3  # Density of the graph (30% dense)
    graph = generateGraph(n, m)
    
    print("Graph:")
    print(graph)
    
    print("\nMinimum Spanning Tree (PrimAPQ):")
    mst_prim_apq = PrimAPQ(graph)
    for edge in mst_prim_apq:
        print(edge)
    
