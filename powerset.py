array = [1,2,3]
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def powerSet(array):
  subset = [[]]
  for el in array:
    for i in range(len(subset)):
      currentSubset = subset[i]
      subset.append(currentSubset + [el])
  return subset

print(powerSet(array))
