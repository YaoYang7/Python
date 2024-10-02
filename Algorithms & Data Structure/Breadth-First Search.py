"""Breadth-First Search => BFS 
    breadth = broad/wide queue 
    -> visit node at same level before progressing
"""

from collections import deque

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'F'],
  'C' : ['G'],
  'D' : [],
  'E' : [],
  'F' : ['H'],
  'G' : ['I'],
  'H' : [],
  'I' : []
}

def bfs(graph, node):
    #Reason for set(): 'n not in visited' below is O(1) instead of O(n).
    visited = set()
    queue = deque()

    visited.add(node)
    queue.append(node)

    while queue:
        # pop left is O(1). For an array, pop(0) is O(n). Hence the change to deque from array.
        s = queue.popleft()
        print(s, end = ' ')

        for n in graph[s]:
            # Because visited is a set, this lookup is O(1).
            if n not in visited:
                visited.add(n)
                queue.append(n)


def main():
    bfs(graph, 'A')

main()

"""
Time complexity:
    O (total number of vertices + total number of edges)
"""