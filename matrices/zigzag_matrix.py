matrix = [[1,2,3], 
          [4,5,6]]

# [1, 2, 3, 6, 5, 4]

def zigzag(matrix):
  result = []
  for i in range(len(matrix)):
    if i % 2 == 0:
      for j in range(len(matrix[0])):
        result.append(matrix[i][j])
    else:
      for j in reversed(range(len(matrix[0]))):
        result.append(matrix[i][j])

  return result


print(zigzag(matrix))
