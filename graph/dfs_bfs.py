# adjacency matrix
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def traverseGraph(graph, current_node):
    print(current_node)
    for child in graph[current_node]:
        traverseGraph(graph, child)
    


# traverseGraph(graph,'A')

from collections import deque
def traverse_bfs(graph, current_node):
    queue = deque([current_node])
    while queue:
        node = queue.popleft()
        print(node)
        for child in graph[node]:
            queue.append(child)

traverse_bfs(graph, 'A')


def traverse_bfs_levels(graph, current_node):
    queue = deque([[current_node]])
    while queue:
        nodes = queue.popleft()
        print(' '.join(nodes))
        nextLevel = []
        for node in nodes:
            for child in graph[node]:
                nextLevel.append(child)
        if nextLevel: queue.append(nextLevel)

traverse_bfs_levels(graph, 'A')

# A
# B C
# D E
# F
#   F

#      A
#    B        C
# D    E         F
