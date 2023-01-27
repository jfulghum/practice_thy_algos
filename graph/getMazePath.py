
'''
You're given a 2d array with 1's and 0's. 1's represent walls, and 0's represent open, walkable space. A robot starts on the top left and goes down to the bottom right. This robot can move in the NSEW direction.

Output the shortest path a robot should take from the top left to the bottom right. If there are multiple shortest paths, any path is valid. If there is no valid path, return None/null.
 

EXAMPLE(S)
Maze:
0 0 0 0
1 1 0 0
0 0 0 1
0 1 1 0
0 0 0 0

getMazePath(maze) -> [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)]

Explanation: The robot needs to travel around the two rows of walls. We're representing the path returned by annotating it with Xs.
x x x 0
1 1 x 0
x x x 1
x 1 1 0
x x x x


Example.  
[[0]] -> [(0, 0)]
[[1]] -> None
[[1],[0]] -> None
[[0,1],[0,0]] -> [(0, 0), (1,0), (1,1)]


Approach:
possible_route = []
within the bounds of the matrix, 
    check one down, right, left and up
    if curr spot is 0, add the tuple to the possible route 
        # check one down, right, left and up, on curr spot

for route in possible_routes:
    if route[-1] == (len(row), len(matrix)):
        valid_route.append(route)

return shortest route in valid_route


FUNCTION SIGNATURE

'''
#   1
# /   \
# 2    3

# [[1,2,3], 
#  [1,2,3]]

# def getMazePath(maze):
#     if maze is None:
#         return None

#     possible_route = []

#     num_rows = len(maze)
#     num_cols = len(maze[0])
#     i, j = 0, 0
#     def traverse(maze, i, j):
#         while i < num_rows:
#             while j < num_cols:
#                 curr_path = (i, j)
#                 if maze[i][j] == 0:
#                     possible_route.append(curr_path)
#                     if i < num_rows and j < num_cols:
#                         i+=1
#                         curr_path = (i, j)
#                         traverse(maze, i, j)

# 0 0 0 0
# 1 1 0 0
# 0 0 0 1
# 0 1 1 0
# 0 0 0 0

from collections import deque      

def bfs(maze):
    if maze is None:
        return None
    path = [(0,0)]
    queue = deque([(path, 0, 0)])
    visited = set()
    visited.add((0,0))
    while queue:
        
        size = len(queue)
        for _ in range(size):
            path, x, y = queue.popleft()
 
            if x == len(maze) and y == len(maze[0]):
                return path

            if x < len(maze) and x >= 0 and y < len(maze[0]) and y >= 0 and maze[x][y] == 0:
                
                
                if (x+1, y) not in visited:
                    visited.add((x+1,y))
                    queue.append([path + [(x+1, y)], x+1, y])
                if (x-1, y) not in visited:
                    visited.add((x-1,y))
                    queue.append([path + [(x-1, y)], x-1, y])
                if (x, y+1) not in visited:
                    visited.add((x,y+1))
                    queue.append([path + [(x, y+1)], x, y+1])
                if (x, y-1) not in visited:
                    visited.add((x,y-1))
                    queue.append([path + [(x, y-1)], x, y-1])

maze =  [[0,0,0], 
         [1,0,0]]

print(bfs(maze))

from collections import deque

def get_neighbors(maze, i, j):
    neighbors = set()
    if i > 0 and maze[i-1][j] != 1:
        neighbors.add((i -1, j))
    if i < len(maze) - 1 and maze[i+1][j] != 1:
        neighbors.add((i + 1, j))
    if j > 0 and maze[i][j-1] != 1:
        neighbors.add((i, j - 1))
    if j < len(maze[0]) - 1 and maze[i][j+1] != 1:
        neighbors.add((i, j + 1))
    return neighbors

def getMazePath(maze):
    if len(maze) == 0:
        return []
    if len(maze[0]) == 0:
        return []

    q = deque()
    visited = set()
    # Seed with the current node and path
    start_node = (0, 0)
    start_path = [(0, 0)]
    q.append((start_node, start_path))
    visited.add((0, 0))

    target = (len(maze) - 1, len(maze[0]) - 1)
    while q:
        curr_node, path = q.popleft()
        if curr_node == target:
            return path
        neighbors = get_neighbors(maze, curr_node[0], curr_node[1])
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                newpath = list(path)
                newpath.append(neighbor)
                q.append((neighbor, newpath))
    return None









