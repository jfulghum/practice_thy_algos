def bsearch(array, target, low, high):
  if high >= low:
    mid = (high + low) // 2 
    if target == array[mid]:
      return mid
    elif target < array[mid]:
      return bsearch(array, target, low, mid - 1)
    else:
      return bsearch(array, target, mid + 1, high)
  else:
    return -1


array = [1,2,3,4,5,6,7,8,9]
print(bsearch(array,8, 0, len(array) - 1))


def binarysearch(array, target):
  left = 0
  right = len(array) - 1
  while left <= right:
    mid = (left + right )//2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return - 1


print(binarysearch(array,8))
