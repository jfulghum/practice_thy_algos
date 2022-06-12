# Write functions that take a multidimensional array as input and then output a single dimensional array. 
matrix = [
  [1, 2, 3],
  [4, 5, 6]
]

# Start with the elements in increasing row major order, meaning the first row from beginning to end, then the second row, etc. 
def template(matrix):
  result = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      result.append(matrix[i][j])
  return result

print(template(matrix)) # [1, 2, 3, 4, 5, 6]
 
# Then move on to column major, which is the first column from beginning to end and then the second, etc.

def template(matrix):
  result = []
  for j in range(len(matrix[0])):
    for i in range(len(matrix)):
      result.append(matrix[i][j])
  return result

print(template(matrix)) # [1, 4, 2, 5, 3, 6]


# As a final challenge, do additional versions where each row is output backward but the rows are in order and similar for columns. 

def template(matrix):
  result = []
  for i in reversed(range(len(matrix))):
    for j in range(len(matrix[0])):
      result.append(matrix[i][j])
  return result

print(template(matrix)) # [4, 5, 6, 1, 2, 3]

# There are actually 4 different variations for both row and column major, so 8 total. Do you see why?
