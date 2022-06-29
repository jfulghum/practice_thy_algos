'''
In mathematics when two matrices are multiplied the result is a new matrix where each position (i, j) in the
output is the sum of the products of the ith row in the first matrix and the jth column in the second. This is
called the cross product.

For example:

1st - row     2nd - col
[1 2]        [5 6]       [19 22]
[3 4]   x    [7 8]   =   [43 50]

The (0, 0) position in the result is: (1 * 5) + (2 * 7) = 19
The (0, 1) position in the result is: (1 * 6) + (2 * 8) = 22
The (1, 0) position in the result is: (3 * 5) + (4 * 7) = 43
The (1, 1) position in the result is: (3 * 6) + (4 * 8) = 50

This makes the complete output:

[19 22]
[43 50]


High-level Approach:
result = [[0, 0], [0, 0]]

i = j = 0
current = 0
value = 0
while i < len(a) - 1:
    j = current
    value = 0
    while j < len(a[0]) -1:
        value += (a[i][j] * b[j][i])
        j += 1
    result[i][current] = value
    current + 1

i = 0
j = 1
1) value += (1 * 5) = 5
2) value += (2 * 7) = 14 = 19


'''
# O(n) * square root of N 

def matrixMultiply(a: list[list[int]], b: list[list[int]]):
    result = [[0] * len(a)  for i in range(len(a))]

    for i in range(len(a)):
        for j in range(len(a)):
            value = 0
        
            for k in range(len(a)):
                value += (a[i][k] * b[k][j])

            result[i][j] = value

    return result



# result 0, 0
# result 0, 1
# result 1, 0
# result 1, 1

# 0, 0
# 0, 1
# 1, 0
# 1, 1


# result 0, 1
# result 1, 1
 


# Test Cases
a = [
  [1, 2],
  [3, 4]
]

b = [
  [5, 6],
  [7, 8]
]

print(matrixMultiply(a, b))
# Answer: [[19, 22], [43, 50]]
