array = [3,4,5,6,7,6,5,4,1,2,3]

def insertionSort(array):
  for i in range(1, len(array)):
    while array[i- 1] > array[i] and i > 0:
      swap(array, i, i - 1)
      i -= 1
  return array

def swap(array, i, j):
  array[i], array[j] = array[j], array[i]

print(insertionSort(array))
