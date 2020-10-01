def bubbleSort(array):
  n = len(array)
  for i in range(n):
    for j in range(n-1-i):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j+1], array[j]
  return array


print(bubbleSort([2,3,4,3,2,1,2,3,6]))
