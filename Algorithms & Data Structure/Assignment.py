import random
import time
import heapq

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
        self._AdjacencyMap[vertex1].append((vertex2, weight)) # linked vertex, weight represent one edge of the vertex
        self._AdjacencyMap[vertex2].append((vertex1, weight))

    def prim_apq_heap(self):
        visited = set()
        priorityQueue = []  # Priority queue to store edges (weight, vertex1, vertex2)
        mst = []  # Minimum spanning tree

        # Initialize with the start vertex
        vertices = list(graph._AdjacencyMap)
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
    
    def prim_apq_unsorted_list(self):
        mst = []
        visited = set()
        priorityQueue = []

        vertices = list(graph._AdjacencyMap)
        start_vertex = vertices[0]
        visited.add(start_vertex)

        for v, weight in self._AdjacencyMap[start_vertex]:
            priorityQueue.append((start_vertex, v, weight))

        while priorityQueue:
            priorityQueue.sort(key=lambda x: x[2])  # Sort the unsorted list based on edge weight
            u, v, weight = priorityQueue.pop(0)

            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                for next_v, next_weight in self._AdjacencyMap[v]:
                    if next_v not in visited:
                        priorityQueue.append((v, next_v, next_weight))

        return mst

class GraphHelper:
    @staticmethod
    # creating a random graph
    def generateGraph(n, m): # n = number of vertices, m = number of edges
        graph = Graph()

        #adding vertices
        for i in range(n): 
            vertex = "Vertex" + str(i);
            graph.add_vertex(vertex) # add vertex to graph, Vertex1 to Vertexn-1
            vertices = list(graph._AdjacencyMap)
            if len(vertices) > 1:
                vertexToLink = vertex
                while(vertex == vertexToLink):
                    vertexToLink = random.choice(vertices)
                weight = random.randint(1, 20)
                graph.add_edge(vertex, vertexToLink, weight)

        #add remaining edges(if available)
        additionalEdges = m - n - 1
        if additionalEdges > 0 :
            for i in range(additionalEdges):
                vertex1 = random.choice(vertices)
                vertex2 = random.choice(vertices)
                weight = random.randint(1, 20)

                # N.B. if vertices are the same move to next iteration, that's because you can enter a situation in which no more edges can be added 
                if vertex1 != vertex2 and vertex1 not in graph._AdjacencyMap[vertex2] and vertex2 not in graph._AdjacencyMap[vertex1]:
                    graph.add_edge(vertex1, vertex2, weight)

        return graph

if __name__ == "__main__":
    
    vertices = [10, 20, 50, 100, 200]

    print("----------------------------------------------------------------------------------------")
    for n in vertices:
        print("----------------------------------------------------------------------------------------")
        print("Vertices: ", n)
        
        #the floor division // rounds the result down to the nearest whole number
        m = ( (n*(n-1)) // 2 ) // 4 # 25% of the maximum number of edges

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
        mst = graph.prim_apq_unsorted_list()
        e3 = time.perf_counter()
        print(f"Prim APQ Unsorted List on low density graph of 25% : ({e3-s3} seconds)")
    print("----------------------------------------------------------------------------------------")

    for n in vertices:
        print("----------------------------------------------------------------------------------------")
        print("Vertices: ", n)
        
        #the floor division // rounds the result down to the nearest whole number
        m = ( (n*(n-1)) // 2 ) // 2 # 50% of the maximum number of edges

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
        mst = graph.prim_apq_unsorted_list()
        e3 = time.perf_counter()
        print(f"Prim APQ Unsorted List on medium density graph of 50% : ({e3-s3} seconds)")
    print("----------------------------------------------------------------------------------------")

    for n in vertices:
        print("----------------------------------------------------------------------------------------")
        print("Vertices: ", n)
        
        #the floor division // rounds the result down to the nearest whole number
        m = ( 9 * (n*(n-1)) // 20 ) # 90% of the maximum number of edges

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
        mst = graph.prim_apq_unsorted_list()
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
