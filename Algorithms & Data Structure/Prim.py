import random
import time
import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_list[vertex1].append((vertex2, weight))
        self.adjacency_list[vertex2].append((vertex1, weight))

class GraphHelper:
    @staticmethod
    def generate_random_graph(n, m):
        graph = Graph()

        for i in range(n):
            graph.add_vertex(i)
            if i > 0 : # doesn't make sense with just one node
                prev_vertex = random.randint(0, i - 1)
                weight = random.randint(1, 20)
                graph.add_edge(i, prev_vertex, weight)

        for j in range(n - 1, m):
            vertex1 = random.randint(0, n - 1)
            vertex2 = random.randint(0, n - 1)
            weight = random.randint(1, 20)

            if vertex1 != vertex2 and vertex1 not in graph.adjacency_list[vertex2] and vertex2 not in graph.adjacency_list[vertex1]:
                graph.add_edge(vertex1, vertex2, weight)

        return graph



def prim_mst_builtin_heap(graph):
    V = len(graph.adjacency_list)
    pq = [(0, 0)]  # Min-heap to store (key, vertex) pairs
    keys = [float('inf')] * V
    in_mst = [False] * V
    parent = [-1] * V

    # Start with vertex 0
    keys[0] = 0

    while pq:
        _, u = heapq.heappop(pq)
        in_mst[u] = True

        for v, weight in graph.adjacency_list[u]:
            if not in_mst[v] and keys[v] > weight:
                keys[v] = weight
                heapq.heappush(pq, (keys[v], v))
                parent[v] = u
        
    print("prim_mst_builtin_heap Minimum Spanning Tree (MST):")
    for v in range(1, V):
        print(f"{parent[v]} - {v}")

def prim_mst_unsorted_list(graph):
    V = len(graph.adjacency_list)
    keys = [float('inf')] * V
    in_mst = [False] * V
    parent = [-1] * V

    # Start with vertex 0
    keys[0] = 0

    while True:
        # Find the minimum key vertex not yet in MST
        u = None
        for v in range(V):
            if not in_mst[v] and (u is None or keys[v] < keys[u]):
                u = v

        if u is None:
            break

        in_mst[u] = True

        for v, weight in graph.adjacency_list[u]:
            if not in_mst[v] and keys[v] > weight:
                keys[v] = weight
                parent[v] = u

    print("prim_mst_unsorted_list Minimum Spanning Tree (MST):")
    for v in range(1, V):
        print(f"{parent[v]} - {v}")

if __name__ == "__main__":
    
    while True :
        print(f"----------------------")
        n = int(input("Insert number of vertices:"))   # Number of vertices
        m = int(input("Insert number of edges:"))  # Number of edges
        print(f"----------------------")
   
        start1 = time.time()
        graph = GraphHelper.generate_random_graph(n, m)
        end1 = start2 = time.time()
        print(f"----------------------")
        mst = prim_mst_builtin_heap(graph)
        print(f"----------------------")
        end2 = start3 = time.time()
        print(f"----------------------")
        mst = prim_mst_unsorted_list(graph)
        print(f"----------------------")
        end3 = time.time()
    
        print(mst)

        print(f"----------------------")
        print(f"Performance time")
        print(f"Graph generation {end1-start1} seconds")
        print(f"prim_mst_builtin_heap {end2-start2} seconds")
        print(f"prim_mst_unsorted_list {end3-start3} seconds")
        print(f"----------------------")
