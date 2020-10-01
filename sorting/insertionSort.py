array = [5,4,3,2]

def insertionSort(array):
  for i in range(1, len(array)):
    while array[i- 1] > array[i] and i > 0:
      print(array)
      array[i], array[i- 1] = array[i -1], array[i]
      i -= 1
  return array

print(insertionSort(array))
