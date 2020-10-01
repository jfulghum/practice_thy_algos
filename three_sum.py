output = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

def three_sum(array, targetSum):
  triplets = []
  array.sort()
  for i in range(len(array) -2 ):
    left = i + 1
    right = len(array) - 1
    while left < right:
      currentSum = array[i] + array[left] + array[right]
      if currentSum == targetSum:
        triplets.append([array[i], array[left],array[right]])
        left += 1
        right -= 1
      elif currentSum > targetSum:
        right -= 1
      else:
        left += 1
  return triplets


print(three_sum(array, targetSum) == output)
