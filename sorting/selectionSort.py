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


# Here is another way. Important thing to remember is for current Index, you must stop 1 before the end. 
#Eg. for currentIdx in range(0, len(array) -1 ):  or while currentIdx < len(array) - 1:
  # Otherwise if you go to the VERY end, you're going to be switching the last one out of order. 
  
  #You also must reset smallestIdx within the first while loop. 
  
def selectionSort(array):
  for currentIdx in range(0, len(array) -1):
    smallestIdx = currentIdx # must reset smallestIdx
    for i in range(currentIdx, len(array)):
      if array[i] < array[smallestIdx]:
        smallestIdx = i
    array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
  return array

# Test Cases
print(selectionSort([]) == [])
print(selectionSort([1]) == [1])
print(selectionSort([3, 1, 2, 4])  == [1, 2, 3, 4])
print(selectionSort([-10, 1, 3, 8, -13, 32, 9, 5]) == [-13, -10, 1, 3, 5, 8, 9, 32])
print(selectionSort([4,5,4,5,4,54]) == [4, 4, 4, 5, 5, 54])
