matrix = [
  [1,0,1],
  [1,0,1],
  [1,0,1],
]

def riverSizes(matrix):
  sizes = []
  visited = [[False for x in row] for row in matrix ]
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      # currentNode = matrix[i][j]
      traverseNodes(matrix, i, j, visited, sizes)
  return sizes

def traverseNodes(matrix, i, j, visited, sizes):
  currentRiverSize = 0
  nodesToExplore = [[i,j]]
  while nodesToExplore: #try removing len later
    currentNode = nodesToExplore.pop()
    i = currentNode[0]
    j = currentNode[1]
    if visited[i][j]: continue
    visited[i][j] = True
    if not matrix[i][j]: continue
    currentRiverSize += 1
    neighborNodes = exploreNodes(i,j,matrix, visited)
    for node in neighborNodes:
      nodesToExplore.append(node)
  if currentRiverSize:
    sizes.append(currentRiverSize)

def exploreNodes(i,j,matrix,visited):
  neighborNodes = []
  if i > 0 and not visited[i-1][j]:
    neighborNodes.append([i-1,j])
  elif i < len(matrix) - 1 and not visited[i+1][j]:
    neighborNodes.append([i+1,j])
  elif j < len(matrix) - 1 and not visited[i][j+1]:
    neighborNodes.append([i,j+1])
  elif j > 0 and not visited[i][j-1]:
    neighborNodes.append([i,j-1])
  return neighborNodes

print(riverSizes(matrix))
