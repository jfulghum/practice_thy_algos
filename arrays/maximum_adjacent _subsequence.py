def kadanesAlgorithm(array):
    maxRunningSum = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        maxRunningSum = max(maxRunningSum + array[i], array[i])
        maxSoFar = max(maxSoFar, maxRunningSum)
    return maxSoFar
