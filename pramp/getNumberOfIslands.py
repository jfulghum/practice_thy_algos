def pushIfValid(q, rows, cols, x, y):
   if (x >= 0 and x < rows and y >= 0 and y < cols):
      q.append([x,y])

def markIsland(i, j, m, rows, cols):
  q = []
  q.append([i,j])
  while len(q) > 0:
    item = q.pop()
    x = item[0]
    y = item[1]
    if m[x][y] == 1:
      m[x][y] = -1
      pushIfValid(q, rows, cols, x - 1, y)
      pushIfValid(q, rows, cols, x, y - 1)
      pushIfValid(q, rows, cols, x + 1, y)
      pushIfValid(q, rows, cols, x, y + 1)

def get_number_of_islands(binaryMatrix):
  m = binaryMatrix
  rows = len(m)
  cols = len(m[0])
  islands = 0

  for i in range(0, rows):
    for j in range(0, cols):

      if m[i][j] == 1:
        markIsland(i, j, m, rows, cols)
        islands += 1

  return islands


