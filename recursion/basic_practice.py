

def factorial(n):
  if n != 1:
    n *= factorial(n - 1)

  return n


print(factorial(3) == 6)
print(factorial(5) == 120)


def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i

  return result 


print(factorial(3) == 6)
print(factorial(5) == 120)



def recursiveMax(arr, curMax = float('-inf'), i = 0):

  if i == len(arr):
    return curMax
    
  if arr[i] > curMax:
    curMax = arr[i]
    

  if i < len(arr):
    return recursiveMax(arr, curMax, i + 1)
  


print(recursiveMax([2,2,55]))
