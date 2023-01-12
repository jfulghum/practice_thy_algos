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


# this is a VERY useful pattern - just by going through it by iterating, it's like you ARE popping left, you are going FIFO

def traverse_bfs_levels2(graph, current_node):
    queue = deque([current_node])
    while queue:
        next_q = []
        for node in queue:
            print(node, end=' ')
            for child in graph[node]:
                next_q.append(child)
        print()
        queue = next_q
