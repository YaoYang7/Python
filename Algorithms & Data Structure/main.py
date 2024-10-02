import random
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


class AdaptablePriorityQueueList:
    def __init__(self):
        self._body = []  
        self._size = 0        

    def __str__(self):
        return str([str(elt) for elt in self._body])
    
    def len(self):
        return len(self._body)
    
    def add(self, key, item):
        elt = Element(key, item, len(self._body))
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
        self._body.pop()      
    
    def isEmpty(self):
        return self._size == 0
        
    def length(self):
        return self._size

class Graph:
    def __init__(self):
        self._AdjacencyMap = dict()

    def __str__(self):
        string = ""
        for vertex in self._AdjacencyMap:
            for connectedVertex, weight in self._AdjacencyMap[vertex]:
                string += "Link: " + str(vertex) + " - " + str(connectedVertex) + " | link weight: " + str(weight) + "\n"
            string += "\n"
        return string

    def add_vertex(self, data):
        self._AdjacencyMap[data] = list()

    def add_edge(self, vertex1, vertex2, weight):
        self._AdjacencyMap[vertex1].append((vertex2, weight))
        self._AdjacencyMap[vertex2].append((vertex1, weight))

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

class GraphHelper:
    @staticmethod
    def generateGraph(n, m):
        graph = Graph()

        for i in range(n):
            vertex = "Vertex" + str(i)
            graph.add_vertex(vertex)
            vertices = list(graph._AdjacencyMap)
            if len(vertices) > 1:
                vertexToLink = vertex
                while vertex == vertexToLink:
                    vertexToLink = random.choice(vertices)
                weight = random.randint(1, 20)
                graph.add_edge(vertex, vertexToLink, weight)

        additionalEdges = m - n - 1
        if additionalEdges > 0:
            for i in range(additionalEdges):
                vertex1 = random.choice(vertices)
                vertex2 = random.choice(vertices)
                weight = random.randint(1, 20)
                if vertex1 != vertex2 and vertex1 not in graph._AdjacencyMap[vertex2] and vertex2 not in graph._AdjacencyMap[vertex1]:
                    graph.add_edge(vertex1, vertex2, weight)

        return graph

def Prims(g, apq):
    q = apq()  
    tree = []
    locs = {}
    for v in g._AdjacencyMap:
        element = q.add(float("inf"), [v, None])
        locs[v] = element

    while not q.isEmpty():
        c = q.remove_min()[1]  
        locs.pop(c[0])

        if c[1] is not None:
            tree.append(c[1])

        for e2 in g._AdjacencyMap[c[0]]:
            v2 = e2[0]
            if v2 in locs:
                cost = e2[1]
                if cost < q.get_key(locs[v2]):
                    q.update_key(locs[v2], cost)
                    locs[v2]._value[1] = e2

    return tree

if __name__ == "__main__":
    vertices = [10, 20, 50, 100, 200, 500, 1000]

    print("----------------------------------------------------------------------------------------")
    for n in vertices:
        print("----------------------------------------------------------------------------------------")
        print("Vertices: ", n)
        
        # The floor division // rounds the result down to the nearest whole number
        m = ((n*(n-1)) // 2) // 4  

        print("Generating low density graph with 25% of the maximum number of edges")
        s1 = time.perf_counter()
        graph = GraphHelper.generateGraph(n, m)
        e1 = time.perf_counter()
        print(f"Graph generated({e1-s1} seconds)")

        s2 = time.perf_counter()
        mst = graph.prim_apq_heap()
        e2 = time.perf_counter()
        print(f"Prim APQ Heap on low density graph of 25% :({e2-s1} seconds)")

        s3 = time.perf_counter()
        mst = Prims(graph, AdaptablePriorityQueueList)
        e3 = time.perf_counter()
        print(f"Prim APQ Unsorted List on low density graph of 25% : ({e3-s3} seconds)")
    print("----------------------------------------------------------------------------------------")

    for n in vertices:
        print("----------------------------------------------------------------------------------------")
        print("Vertices: ", n)
        
        # The floor division // rounds the result down to the nearest whole number
        m = ((n*(n-1)) // 2) // 2  

        print("Generating low density graph with 50% of the maximum number of edges")
        s1 = time.perf_counter()
        graph = GraphHelper.generateGraph(n, m)
        e1 = time.perf_counter()
        print(f"Graph generated({e1-s1} seconds)")

        s2 = time.perf_counter()
        mst = graph.prim_apq_heap()
        e2 = time.perf_counter()
        print(f"Prim APQ Heap on medium density graph of 50% :({e2-s1} seconds)")

        s3 = time.perf_counter()
        mst = Prims(graph, AdaptablePriorityQueueList)
        e3 = time.perf_counter()
        print(f"Prim APQ Unsorted List on medium density graph of 50% : ({e3-s3} seconds)")
    print("----------------------------------------------------------------------------------------")

    for n in vertices:
        print("----------------------------------------------------------------------------------------")
        print("Vertices: ", n)
        
        # The floor division // rounds the result down to the nearest whole number
        m = (9 * (n*(n-1)) // 20)  

        print("Generating high density graph with 90% of the maximum number of edges")
        s1 = time.perf_counter()
        graph = GraphHelper.generateGraph(n, m)
        e1 = time.perf_counter()
        print(f"Graph generated({e1-s1} seconds)")

        s2 = time.perf_counter()
        mst = graph.prim_apq_heap()
        e2 = time.perf_counter()
        print(f"Prim APQ Heap on high density graph of 90% :({e2-s1} seconds)")

        s3 = time.perf_counter()
        mst = Prims(graph, AdaptablePriorityQueueList)
        e3 = time.perf_counter()
        print(f"Prim APQ Unsorted List on high density graph of 90% : ({e3-s3} seconds)")
    print("----------------------------------------------------------------------------------------")

    # Uncomment these 3 lines and put it into the for loops to print out the graph
    # print(f"----------------------")
    # print("Display graph:")
    # print(graph)

    # Uncomment these lines and put it into the for loops to print out the MST
    # print("----------------------")
    # print("MST output with Prim APQ Heap:")
    # for vertex1, vertex2, weight in mst:
    #     print(f"{vertex1} - {vertex2} | weight: {weight}")

    # print("----------------------")
    # print("MST output with Prim APQ Unsorted List:")
    # for vertex1, vertex2, weight in mst:
    #     print(f"{vertex1} - {vertex2} | weight: {weight}")
