# Given a two dimensional matrix (NxM), a size A such that A is less than both N and M, and an offset X, Y, 
# return a new matrix that is the sub-matrix of the original. The size of the new matrix is AxA (square) 
# and the values should be those in the original matrix starting at position indicated by the offset (X, Y). For example for an input matrix:

# 1 2 3
# 4 5 6
# 7 8 9
# Size is 2 and offset is (0, 1), the expected output is:

# 2 3
# 5 6
# Because the output is size 2x2 and is taken from a submatrix whose top left corner is at (0, 1) in the original.

# Return an empty array if a square of the required size is not possible at starting at the given offset.
# The input matrix can be assumed to be a consistent rectangle (all rows are the same length).


def solution(matrix, size, x, y):
    if size > len(matrix) or size > len(matrix[0]):
        return []
    if size + x > len(matrix):
        return []
    res = [[0] * size for _ in range(size)]
    temp = y
    for r in range(size):
        y = temp;
        for c in range(size):
            res[r][c] = matrix[x][y]
            y += 1
        x += 1
    return res
