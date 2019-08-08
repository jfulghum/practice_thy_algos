# Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

def kdifference(arr, k):
  result = []
  rec = set(arr)
  for y in arr:
    if (k + y) in rec:
        result.append([k + y, y])
  return result

print(kdifference([0,1,2,3,4],4))
