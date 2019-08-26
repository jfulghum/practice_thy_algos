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

