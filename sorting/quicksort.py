def quicksort(array):
  if len(array) <= 1: return array
  return quicksort([x for x in array[1:] if x < array[0]]) + [array[0]] + quicksort([x for x in array[1:] if x >= array[0]])

print(quicksort([3,2,4,6,5,4,3]))
