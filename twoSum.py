def twoSum(array, target):
  nums = {}
  for el in array:
    potentialMatch = target - el
    if potentialMatch in nums:
        return [potentialMatch, el]
    else:
      nums[el] = True




print(twoSum([1,2,3,4,5,6], 4))
# I want [1,3]
