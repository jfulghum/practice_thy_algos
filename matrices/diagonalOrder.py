
def diagonalOrder(arr, n, m):
  ans = [[] for i in range(n + m - 1)]
   
  for i in range(m):
      for j in range(n):
        ans[i + j].append(arr[j][i])
   
  for i in range(len(ans)):
      for j in range(len(ans[i])):
          print(ans[i][j], end = " ")
      print()
 
# Driver Code
# we have a matrix of n rows
# and m columns

m = 3
n = 4

# ans = [[], [], [], [], [], []]
# Function call
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10,11,12]]
diagonalOrder(arr, n, m)


# 1 
# 4 2 
# 7 5 3 
# 10 8 6 
# 11 9 
# 12 
 
# # Function call
# arr = [[1, 2, 3, 4],[ 5, 6, 7, 8],[9, 10, 11, 12 ],[13, 14, 15, 16 ],[ 17, 18, 19, 20]]
# diagonalOrder(arr, n, m)
