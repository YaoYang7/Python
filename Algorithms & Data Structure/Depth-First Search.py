"""
Depth-First Search => DFS 
    depth = vertical before horizontal stack 
"""
graph = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [],
}

def dfs(graph, node):
    # Reason for set(): 'n not in visited' is O(1) instead of O(n).
    visited = set()
    stack = []

    visited.add(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s, end = ' ')

        # Reverse iterate through the edge list so results match recursive version.
        for n in reversed(graph[s]):
            # Because visited is a set, this lookup is O(1).
            if n not in visited:
                visited.add(n)
                stack.append(n)


def main():
    dfs(graph, 'A')


main()

"""
Time complexity:
    O (total number of vertices + total number of edges)
"""