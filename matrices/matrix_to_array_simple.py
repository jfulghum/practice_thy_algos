# Write functions that take a multidimensional array as input 
# and then output a single dimensional array. 
# Start with the elements in increasing row major order,
# meaning the first row from beginning to end, then the second row, etc. 
# Then move on to column major, which is the first column from beginning to end and then the second, etc.
matrix = [[1,2,3], 
          [4,5,6]]

def matrix_to_array_row_major(matrix):
  array = []
  for i in range(len(matrix)): #rows
    for j in range(len(matrix[0])): #cols
      array.append(matrix[i][j])

  return array

print(matrix_to_array_row_major(matrix))


def matrix_to_array_col_major(matrix):
  array = []
  for j in range(len(matrix[0])): #cols
    for i in range(len(matrix)): #rows
      array.append(matrix[i][j])

  return array

print(matrix_to_array_col_major(matrix))
