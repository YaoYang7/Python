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

class Vertex:
    def __init__(self, element):
        self._element = element

    def __str__(self):
        return str(self._element)

class Edge:
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

# Unsorted list
class APQ_List:
    def __init__(self):
        self._body = []  
        self._size = 0        

    def __str__(self):
        return str([str(elt) for elt in self._body])
    
    def len(self):
        return len(self._body)
    
    def add(self,key,item):
        elt = Element(key,item,len(self._body))
        self._body.append(elt)
        self._size += 1
        return elt
    
    def min(self):
        minimum = self._body[0]
        for elt in self._body:
            if elt._key < minimum._key:
                minimum = elt
        return minimum

    def remove_min(self):
        m = self.min()
        self._body[m._index], self._body[-1] = self._body[-1], self._body[m._index]
        self._body[m._index]._index, self._body[-1]._index = self._body[-1]._index, self._body[m._index]._index
        self._body.pop()
        self._size -= 1
        return (m._key, m._value)
        
    def update_key(self, element, new_key):
        self._body[element._index]._key = new_key

    def get_key(self, element):
        return self._body[element._index]._key

    def remove(self, element):
        self._body[element._index], self._body[-1] = self._body[-1], self._body[element._index]
        self._body[element._index]._index, self._body[-1]._index = self._body[-1]._index, self._body[element._index]._index
        print(f"removing (  {self._body.pop()}  )")      
    
    def is_empty(self):
        return self._size == 0
        
    def length(self):
        return self._size

class Graph:
    def __init__(self):
        self._AdjacencyMap = dict() # each vertex(Key) maintains (value) a hash-map where the other vertices
                                # are the keys and the incident edges are teh values
        
    def __str__(self):
        string = ""
        for vertex in self._AdjacencyMap:
            for connected_vertex, edge in self._AdjacencyMap[vertex].items():
                string += str(vertex) + str(connected_vertex) + " | " + str(edge) + "\n"
            string += "\n"
        return string
    
    def vertices(self):
        return [str(vertex) for vertex in self._AdjacencyMap.keys()]
    
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
        return [edge for edge in self._AdjacencyMap[vertex].values()] # returns the edges incident to the vertex
    
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

        if (v1 in self._AdjacencyMap and v2 in self._AdjacencyMap[v1]) and (v2 in self._AdjacencyMap and v1 in self._AdjacencyMap[v2]):
            self._AdjacencyMap[v1].pop(v2)
            self._AdjacencyMap[v2].pop(v1)
        else:
            print("Edge not found")

    # def APQ_Heap(self):
    #     visited = set()
    #     priorityQueue = []
    #     mst = []

    #     vertices = list(self._AdjacencyMap.keys())
    #     if not vertices:
    #         return mst  # Return empty mst if no vertices are present in the graph

    #     start_vertex = vertices[0]
    #     visited.add(start_vertex)
    #     for connected_vertex, edge in self._AdjacencyMap[start_vertex].items():
    #         heapq.heappush(priorityQueue, (edge._weight, edge._v1._element, edge._v2._element))  # Assuming _element is a comparable attribute

    #     while priorityQueue:
    #         weight, vertex1, vertex2 = heapq.heappop(priorityQueue)
    #         if vertex2 not in visited:
    #             visited.add(vertex2)
    #             mst.append((vertex1, vertex2, weight))
    #             if vertex2 in self._AdjacencyMap:  # Check if the next vertex exists in the adjacency map
    #                 for next_vertex, edge in self._AdjacencyMap[vertex2].items():
    #                     if next_vertex not in visited:
    #                         heapq.heappush(priorityQueue, (edge._weight, edge._v1._element, edge._v2._element))  # Assuming _element is a comparable attribute

    #     return mst
    
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

    while not q.is_empty():
        c = q.remove_min()[1]  
        locs.pop(c[0])

        if c[1] is not None:
            tree.append(c[1])

        for e2 in graph._AdjacencyMap[c[0]].values():  # Iterate over values (edges) instead of keys
            v2 = e2.opposite(c[0])  # Get the opposite vertex of the edge
            if v2 in locs:
                cost = e2._weight  # Access the weight directly from the edge object
                if cost < q.get_key(locs[v2]):
                    q.update_key(locs[v2], cost)
                    locs[v2]._value[1] = e2

    return tree

#APQ_Heap is not my code, it was implemented with the help of ChatGPT 
class APQ_Heap:
    def __init__(self):
        self._body = []
        self._size = 0

    def __str__(self):
        """ Return a breadth-first string of the values. """
        # method body goes here
        ans = ""
        for i in self._body:
            ans += "k"+str(i._key) + " " + "i"+str(i._index) + " " + "v"+str(i._value) + " "
        return ans

    def add(self, key, value):
        """ Add Element(key,value) to the heap. """
        # method body goes here
        elt = Element(key,value,self._size)
        self._body.append(elt)
        self._upheap(self._size)

        self._size += 1
        return elt

    def min(self):
        """ Return the min priority key,value. """
        # method body goes here
        if self._body:
            return self._body[0]
        else:
            return "None"

    def remove_min(self):
        """ Remove and return the min priority key,value. """
        # method body goes here
        if self._body:
            output = self._body[0]
            if self._size > 1:
                self._body[0] = self._body.pop()
                self._body[0]._index = 0
                if self._size > 1:
                    self._size -= 1
                    self._downheap(0)
            else:
                self._size -= 1
                self._body.pop()
            return (output._key,output._value)
        else:
            return "None"

    def update_key(self,element, new_key):

        if element._key < new_key:
            element._key = new_key
            self._downheap(element._index)
        else:
            element._key = new_key
            self._upheap(element._index)

    def get_key(self,element):
        return self._body[element._index]._key

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def length(self):
        return self._size

    def _upheap(self, posn):
        """ Bubble the item in posn in the heap up to its correct place. """

        item = self._body[posn]
        current_position = posn
        while True:
            parent_position = (current_position - 1) // 2
            if parent_position < 0:
                break
            else:
                if item._key < self._body[parent_position]._key:
                    self._body[current_position], self._body[parent_position] = self._body[parent_position], self._body[current_position]
                    self._body[current_position]._index, self._body[parent_position]._index = self._body[parent_position]._index, self._body[current_position]._index
                    current_position = parent_position
                else:
                    break


    def _downheap(self, idx):
        """ Bubble the item at idx in the heap down to its correct place. """

        current_position = idx
        while True:
            children = [current_position*2+1,current_position*2+2]
            if children[0] >= self._size:
                children[0] = None
            if children[1] >= self._size:
                children[1] = None

            if children[0] and not children[1]:
                min_child = children[0]
            elif children[1] and not children[0]:
                min_child = children[1]
            elif not children[0] and not children[1]:
                break
            else:
                d = {children[0]: self._body[children[0]]._key,children[1]: self._body[children[1]]._key}
                min_child = min(d, key=lambda k: d[k])

            if self._body[current_position]._key > self._body[min_child]._key:
                self._body[current_position], self._body[min_child] = self._body[min_child], self._body[current_position]
                self._body[current_position]._index, self._body[min_child]._index = self._body[min_child]._index, self._body[current_position]._index
                current_position = min_child
            else:
                break


def generateDenseGraph(n=0):
    """
    Generates a max density graph with n vertices (Max density is n(n-1)//2)
    """
    if n == 0:
        n = int(input("Input n: "))
        
    graph = Graph()
    vertices = [None] * n
    
    for num in range(n):
        vertices[num] = graph.add_vertex(num)
        if num > 0:
            rand = randint(0, num - 1)
            graph.add_edge(vertices[num], vertices[rand], randint(1, 20))
    
    i = 0
    while i != n:
        v1 = vertices[i]
        for num1 in range(i, n):
            v2 = vertices[num1]
            if not graph.get_edge(v1, v2) and num1 != i:
                graph.add_edge(v1, v2, randint(1, 20))
        i += 1
    
    return graph

def generateSparseGraph(n=0):
    """Generates a random graph using n as parameter for graph generation"""
    if n == 0:
        n = int(input("Input n: "))
    graph = Graph()
    vertices = [None] * n
    added_edges = set()  # Keep track of added edges to avoid duplicates
    for num in range(n):
        vertices[num] = graph.add_vertex(num)
        if num > 0:
            rand = randint(0, num - 1)
            edge_key = tuple(sorted((vertices[num]._element, vertices[rand]._element)))
            # Check if the edge has already been added
            if edge_key not in added_edges:
                graph.add_edge(vertices[num], vertices[rand], randint(1, 20))
                added_edges.add(edge_key)  # Add the edge to the set of added edges
    return graph

if __name__ == "__main__":
    vertices = [100, 200, 500, 1000, 2000, 5000, 10000, 12000, 14000, 16000, 20000]

    for v in vertices:
        print ("----------------------------------------------------------------------------------------")
        denseGraph = generateDenseGraph(v)
        s1 = time.perf_counter()
        mst = PrimAlgorithm(denseGraph, APQ_Heap)
        e1 = time.perf_counter()
        print (f"Prim APQ Heap on dense graph of {v} vertices: {e1-s1} seconds")
        s2 = time.perf_counter()
        mst = PrimAlgorithm(denseGraph, APQ_List)
        e2 = time.perf_counter()
        print (f"Prim APQ List on dense graph of {v} vertices: {e2-s2} seconds")
        print ("----------------------------------------------------------------------------------------")

    for v in vertices:
        print ("----------------------------------------------------------------------------------------")
        sparseGraph = generateSparseGraph(v)
        s1 = time.perf_counter()
        mst = PrimAlgorithm(sparseGraph, APQ_Heap)
        e1 = time.perf_counter()
        print (f"Prim APQ Heap on sparse graph of {v} vertices: {e1-s1} seconds")
        s2 = time.perf_counter()
        mst = PrimAlgorithm(sparseGraph, APQ_List)
        e2 = time.perf_counter()
        print (f"Prim APQ List on sparse graph of {v} vertices: {e2-s2} seconds")
        print ("----------------------------------------------------------------------------------------")