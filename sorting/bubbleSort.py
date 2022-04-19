def bubbleSort(array):
  n = len(array)
  for i in range(n):
    for j in range(n-1-i):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j+1], array[j]
  return array


print(bubbleSort([2,3,4,3,2,1,2,3,6]))



#here's another (i think simpler) way:

def bubbleSort(array):
  i = 0 
  while i < len(array):
    for j in range(i + 1, len(array)):
      if array[i] > array[j]:
        array[i], array[j] = array[j], array[i]
    i += 1 
  return array

print(bubbleSort([34,3,4,2,4,2,3,4]))
