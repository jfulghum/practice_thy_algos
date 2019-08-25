def bsearch(array, target, l, r):
  if r >= l:
    mid = (l + r - 1) //2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      return bsearch(array, target, 0, mid - 1)
    elif array[mid] < target:
      return bsearch(array, target, mid + 1, l + r - 1)
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
