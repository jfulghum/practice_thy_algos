def sortedSquaredArray(array):
	largestIdx = len(array) - 1
	smallestIdx = 0
	result = [0 for _ in array]
    for idx in reversed(range(len(array))):
		smallest = array[smallestIdx]
		largest = array[largestIdx]
		if abs(largest) > abs(smallest):
			result[idx] = largest ** 2
			largestIdx -= 1
		else:
			result[idx] = smallest ** 2
			smallestIdx += 1
	return result
			
