# This means that the first row will be in the output from first to last, but the second row will be the reverse, last to first, then the third is back to normal order again, each row the opposite order of the ones before and after.
matrix = [
  [1, 2, 3],
  [4, 5, 6]
]
 # [1, 2, 3, 6, 5, 4].


def linearizeZigZag(matrix):
  result = []
  for i in range(len(matrix)):
    if i % 2 == 0:
      result.extend(matrix[i])
    else:
      result.extend(reversed(matrix[i]))
  return result


print(linearizeZigZag(matrix)) # [1, 2, 3, 6, 5, 4]
