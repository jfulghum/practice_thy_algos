# Given a two dimensional array of integers, fold this array over a vertical axis, adding the numbers that meet. This means that in each row, the first and last numbers are added to become the first element in the output, and the second and second to last become the second element, etc. For example:

matrix = [[1,2,3, 4], 
         [5,6,7,8]]

answer = [[5,5], [13,13]]

# questions
# Can I mutate the orginal array? No. 
# Do you want a new array back? Yes.

# sudo code
# create a new reversed matrix
# add two matrices together
# remove the second half of the new matrix

def solution(original_matrix):
  max_len = len(original_matrix[0]) // 2
  reversed_matrix = []

  for row in original_matrix:
    new_row = row[::-1]
    reversed_matrix.append(new_row)

  #initialize 
  combined_matrix = [[0 for _ in range(len(original_matrix[0]))] for _ in range(len(original_matrix))]
  
  for i in range(len(combined_matrix)):  
    for j in range(len(combined_matrix[0])):
        combined_matrix[i][j] = original_matrix[i][j] + reversed_matrix[i][j]

  return [row[:max_len] for row in combined_matrix]

print(solution(matrix))# [[5, 5], [13, 13]]

