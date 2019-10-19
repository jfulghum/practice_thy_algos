# Input:
flowerbed = [1,0,0,0,1]
n = 1
# Output: True

# Input:
# flowerbed = [1,0,0,0,1]
# n = 2
# Output: False

def canPlantFlowers(array, n):
  for i in range(len(array)):
    if array[i] == 0 and (i == 0 or array[i - 1] == 0) and (i == len(array) - 1 or array[i + 1] == 0):
      array[i] = 1
      n -= 1
  return n <= 0
print(canPlantFlowers(flowerbed, n))
