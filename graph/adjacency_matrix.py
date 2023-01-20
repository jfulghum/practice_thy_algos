from collections import deque

def matrix_to_list(matrix):
    graph = {}
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph

def solution(matrix, v1, v2):
  adj_list = matrix_to_list(matrix)
  q = deque([(v1, 0)])
  while q:
    current, depth = q.popleft()
    if current == v2: 
        return depth
    for child in adj_list[current]:
      q.append((child, depth +1))
  return -1
