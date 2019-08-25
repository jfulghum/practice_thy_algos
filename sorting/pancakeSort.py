def pancake_sort(arr):
  current_size = len(arr)
  while current_size > 1:
    biggest = biggestIndex(arr[:current_size])
    flip(arr, biggest)
    flip(arr, current_size - 1)
    current_size -= 1
  return arr

[1,2,3,4,56,7] # 4
[56,1,2,3,4,7] #flip first 6
[7,4,3,2,1,56] # find biggest of five 5.
[1,2,3,4,7,56] #flip first 5

def biggestIndex(arr):
  biggest = 0
  for i in range(len(arr)):
    if arr[i] > arr[biggest]:
      biggest = i
  return biggest

def flip(arr, k):
  arr[:k+1] = arr[:k+1][::-1]

arr = [1,2,3,4,56,7]


print(pancake_sort(arr))


#my way
def pancakeSort(array):
  for i in range(len(array)-1,-1,-1):
    biggest = findBiggestIdx(array[:i+1])
    flip(array, biggest)
    flip(array, i)
  return array


def findBiggestIdx(array):
  biggest = 0
  for i in range(len(array)):
    if array[i] > array[biggest]:
      biggest = i
  return biggest


def flip(array, k):
  array[:k+1] = array[:k+1][::-1]

print(pancakeSort([1, 2, 3, 3, 4,4,3,2,1,2,3,4,55,66,43]))
