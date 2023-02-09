# You're given a 2d array with 1's and 0's. 1's represent walls, and 0's represent open, walkable space. A robot starts on the top left and goes down to the bottom right. This robot can move in the NSEW direction.

# Output the shortest path a robot should take from the top left to the bottom right. If there are multiple shortest paths, any path is valid. If there is no valid path, return None/null.
 

# EXAMPLE(S)
# Maze:
# 0 0 0 0
# 1 1 0 0
# 0 0 0 1
# 0 1 1 0
# 0 0 0 0

# getMazePath(maze) -> [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)]

# Explanation: The robot needs to travel around the two rows of walls. We're representing the path returned by annotating it with Xs.
# x x x 0
# 1 1 x 0
# x x x 1
# x 1 1 0
# x x x x

# 0 0 
# 1 0
# -> [(0, 0), (0, 1), (1, 1)]

# Breadth first search -> as soon as you hit bottom right len(martix), row, len(martix[0]) cols

# below is all wrong
# def get_neighbors(i, j, queue, matrix):

    
#   if j + 1 < len(matrix[0]) and matrix[i][j + 1] == 0:
#     queue.append((i, j + 1))

#   if i + 1 < len(matrix) and matrix[i+ 1][j] == 0:
#     queue.append((i + 1, j))

#   if i - 1 > 0 and matrix[i - 1][j] == 0:
#     queue.append((i - 1, j))

#   if j - 1 > 0 and matrix[i][j - 1] == 0:
#     queue.append((i, j - 1))
    
    
    
  
# matrix = [[0,0], [1,0]]

# from collections import deque

# def get_shortest_path(matrix) -> list:
#   first = matrix[0][0]
#   if first == 1:
#     return None
    
#   queue = deque([(0,0)])
#   current_path = []
#   while queue:
#     i, j = queue.popleft()
#     current_path.append((i,j))
#     if (i,j) == (len(matrix), len(matrix[0])):
#       return current_path
#     get_neighbors(i, j, queue, matrix)
#     print(queue)
    


#   return current_path
  
# matrix = [[0, 0, 0, 0],
# [1, 1, 0, 0]]
# # [0, 0, 0, 1],
# [0, 1, 1, 0],
# [0, 0, 0, 0]]
  
print(get_shortest_path(matrix))
