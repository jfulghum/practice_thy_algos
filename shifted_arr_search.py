# A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

# Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

# Explain your solution and analyze its time and space complexities.

def shifted_arr_search(shiftArr, num):
  pivot = find_pivot(shiftArr)

  if pivot == 0 or num < shiftArr[0]:
    return binary_search(shiftArr, num, pivot, len(shiftArr) - 1)
  return binary_search(shiftArr, num, 0, pivot - 1)


otherarr = [19, 2, 4, 5, 9, 12, 17, 18]
arr = [9, 12, 17, 18, 19, 2, 4, 5]
def find_pivot(arr):
  begin = 0
  end = len(arr) - 1
  while begin <= end:
    mid = (begin + end)//2
    if mid == 0 or arr[mid] < arr[mid-1]:
      return mid
    if arr[mid] > arr[0]:
      begin = mid + 1
    else:
      end = mid - 1
  return 0
print(find_pivot(arr))

def binary_search(array, target, begin, end):
  while begin <= end:
    mid = (begin + end)//2
    if array[mid] == target:
      return mid
    elif target < array[mid]:
      end = mid - 1
    else:
      begin = mid + 1
  return -1


#otherarr = [19, 2, 4, 5, 9, 12, 17, 18]
#arr = [9, 12, 17, 18, 19, 2, 4, 5]
#left = shiftArr[0]

