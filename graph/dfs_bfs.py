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
        
 # Example 1:
#                  0   1   2   3
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.

# Example 2:
#                   0      1     2   3
# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

# 1
#set([0, 1, 2, 3]) == len(rooms)

# Input: rooms = [[3],[2],[1],[]]
 def traversal(rooms):
    visited = set([0])
    room1 = rooms[0]
    queue = deque([room1])
    while queue:
        curr_room = queue.popleft()
        for key in curr_room:
            if key not in visited:
                queue.append(rooms[key])
            visited.add(key)
    print('visited', visited)
    return len(visited) == len(rooms)

rooms = [[1,3],[3,0,1],[2],[0]]

print(traversal(rooms)) # False

rooms2 = [[1],[2],[3],[]]

print(traversal(rooms2)) # True
