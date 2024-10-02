from random import randint
import time
import heapq

class Element:
    """ A key, value and index. """
    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def __str__(self):
        return str(self._key) + " " + str(self._value) + " " + str(self._index)

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

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

class APQ_List:
    def __init__(self):
        self._body = []  
        self._size = 0        

    def __str__(self):
        return str([str(element) for element in self._body])
    
    def len(self):
        return len(self._body)
    
    def add(self, key, item):
        element = Element(key, item, len(self._body))
        self._body.append(element)
        self._size += 1
        return element
    
    def min(self):
        minimum = self._body[0]
        for element in self._body:
            if element._key < minimum._key:
                minimum = element
        return minimum

    def remove_min(self):
        minimum = self.min() # gets the minimum 
        self._body[minimum._index], self._body[-1] = self._body[-1], self._body[minimum._index]
        self._body[minimum._index]._index, self._body[-1]._index = self._body[-1]._index, self._body[minimum._index]._index
        self._body.pop()
        self._size -= 1
        return (minimum._key, minimum._value)
        
    def update_key(self, element, new_key):
        self._body[element._index]._key = new_key

    def get_key(self, element):
        return self._body[element._index]._key

    def remove(self, element):
        self._body[element._index], self._body[-1] = self._body[-1], self._body[element._index]
        self._body[element._index]._index, self._body[-1]._index = self._body[-1]._index, self._body[element._index]._index
        self._body.pop()      
    
    def isEmpty(self):
        return self._size == 0
        
    def length(self):
        return self._size

# class APQ_Heap is taken from chatGPT    
class APQ_Heap:
    def __init__(self):
        self._body = []  
        self._size = 0        
        self._locator = {}

    def __str__(self):
        return str([str(element) for element in self._body])
    
    def len(self):
        return len(self._body)
    
    def add(self, key, item):
        element = Element(key, item, len(self._body))
        self._body.append(element)
        self._size += 1
        self._locator[item] = element
        heapq.heappush(self._body, element)
        return element
    
    def min(self):
        return self._body[0]

    def remove_min(self):
        minimum = heapq.heappop(self._body)
        self._size -= 1
        del self._locator[minimum._value]
        return (minimum._key, minimum._value)
        
    def update_key(self, element, new_key):
        element._key = new_key
        heapq._siftdown(self._body, 0, element._index)

    def get_key(self, element):
        return element._key

    def remove(self, element):
        index = element._index
        last = self._body.pop()
        if index != len(self._body):
            self._body[index] = last
            self._locator[last._value] = last
            heapq._siftup(self._body, index)

    def isEmpty(self):
        return self._size == 0
        
    def length(self):
        return self._size

class Graph():
    def __init__(self):
        self._AdjacencyMap = dict() # each vertex(Key) maintains (value) a hash-map where the other vertices
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
        for vertex in self._AdjacencyMap:
            for edge in self._AdjacencyMap[vertex]:
                edges.add(str(self._AdjacencyMap[vertex][edge]))
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


    def prim_apq_heap(self):
        visited = set()
        priorityQueue = []  
        mst = []  

        vertices = list(self._AdjacencyMap)
        start_vertex = vertices[0]
        visited.add(start_vertex)
        for connected_vertex, weight in self._AdjacencyMap[start_vertex]:
            heapq.heappush(priorityQueue, (weight, start_vertex, connected_vertex))

        while priorityQueue:
            weight, vertex1, vertex2 = heapq.heappop(priorityQueue)
            if vertex2 not in visited:
                visited.add(vertex2)
                mst.append((vertex1, vertex2, weight))
                for next_vertex, next_weight in self._AdjacencyMap[vertex2]:
                    if next_vertex not in visited:
                        heapq.heappush(priorityQueue, (next_weight, vertex2, next_vertex))

        return mst

# This is my original implementation of the Graph class and the GraphHelper class but then I changed it back to just the standard Graph class
# class GraphHelper:
#     @staticmethod
#     def generateGraph(n, m):
#         graph = Graph()

#         for i in range(n):
#             vertex = "Vertex" + str(i)
#             graph.add_vertex(vertex)
#             vertices = list(graph._AdjacencyMap)
#             if len(vertices) > 1:
#                 vertexToLink = vertex
#                 while vertex == vertexToLink:
#                     vertexToLink = random.choice(vertices)
#                 weight = random.randint(1, 20)
#                 graph.add_edge(vertex, vertexToLink, weight)

#         additionalEdges = m - n - 1
#         if additionalEdges > 0:
#             for i in range(additionalEdges):
#                 vertex1 = random.choice(vertices)
#                 vertex2 = random.choice(vertices)
#                 weight = random.randint(1, 20)
#                 if vertex1 != vertex2 and vertex1 not in graph._AdjacencyMap[vertex2] and vertex2 not in graph._AdjacencyMap[vertex1]:
#                     graph.add_edge(vertex1, vertex2, weight)

#         return graph

def PrimAlgorithm(graph, q_method):
    q = q_method()  
    tree = []
    locs = {}
    for v in graph._AdjacencyMap:
        element = q.add(float("inf"), [v, None])
        locs[v] = element

    while not q.isEmpty():
        c = q.remove_min()[1]  
        locs.pop(c[0])

        if c[1] is not None:
            tree.append(c[1])

        for e2 in graph._AdjacencyMap[c[0]]:
            v2 = e2[0]
            if v2 in locs:
                cost = e2[1]
                if cost < q.get_key(locs[v2]):
                    q.update_key(locs[v2], cost)
                    locs[v2]._value[1] = e2

    return tree

def generateDenseGraph(n=0):
    """Generates a max density graph with n vertices (Max density is n(n-1)//2)"""
    if n==0:
        n=int(input("Input n:"))
    graph=Graph()
    l=[None] * n
    for num in range(n):
        l[num]=graph.add_vertex(num)
        if num>0:
            rand=randint(0,num-1)
            graph.add_edge(l[num],l[rand],randint(1,20))
    i=0
    while i!=n:
        v1=l[i]
        for num1 in range(i,n):
            v2=l[num1]
            if not graph.get_edge(v1,v2) and num1!=i:
                graph.add_edge(v1,v2,randint(1,20))
        i+=1
    return graph

def generateSparseGraph(n=0):
    """Generates a random graph using n as parameter for graph generation"""
    if n==0:
        n=int(input("Input n:"))
    graph=Graph()
    l=[None]*n
    for num in range(n):
        l[num]=graph.add_vertex(num)
        if num>0:
            rand=randint(0,num-1)
            graph.add_edge(l[num],l[rand],randint(1,20))

if __name__ == "__main__":
    vertices = [10000, 12000, 14000, 20000]

    # print ("----------------------------------------------------------------------------------------")
    # denseGraph = generateMaxGraph(10)
    # s1 = time.perf_counter()
    # mst = PrimAlgorithm(denseGraph, APQ_Heap)
    # e1 = time.perf_counter()
    # print (f"Prim APQ Heap on dense graph of 10000 vertices: {e1-s1} seconds")
    # s2 = time.perf_counter()
    # mst = PrimAlgorithm(denseGraph, APQ_List)
    # e2 = time.perf_counter()
    # print (f"Prim APQ List on dense graph of 10000 vertices: {e2-s2} seconds")
    # print ("----------------------------------------------------------------------------------------")
    g = generateDenseGraph(10)
    print (g.num_edges())