# Given an array of integers eg [1,2,-3,1] find whether there  is a sub-sequence that sums to 0 and return it (eg 1,2,-3 or 2,-3,1)

def subsequenceSub(array, target):
  current_sum = array[0]
  start = 0
  i = 1
  while i <= len(array):
    while current_sum > target and start < i - 1:
      current_sum = current_sum - array[start]
      start += 1
    if current_sum == target:
      return True
    if i < len(array):
      current_sum += array[i]
    i += 1
  return False

#patrick let's go over this
print(subsequenceSub([1,2,-3,1] , 0))
