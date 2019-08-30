array = [4,5,6,3,1,2,4,5,6]

def selectionSort(array):
  currentIdx = 0
  while currentIdx < len(array) - 1:
    smallestIdx = currentIdx
    for i in range(currentIdx + 1, len(array)):
      if array[i] < array[smallestIdx]:
        smallestIdx = i
    swap(array, currentIdx, smallestIdx)
    currentIdx += 1
  return array

def swap(array, i, j):
  array[i], array[j] = array[j], array[i]

print(selectionSort(array))

#It minimizies number of swaps, choose when swapping is expensive.
