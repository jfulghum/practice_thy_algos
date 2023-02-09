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

from collections import deque

def get_neighbors(maze, i, j):
  pass

def getMazePath(maze):
  pass

maze = [[0,0],
        [1,0],
        [1,0],
        [0,0]]

print(getMazePath(maze)) # [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1)]
