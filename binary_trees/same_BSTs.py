def sameBsts(arrayOne, arrayTwo):
    # idea is 
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    
    leftOne = findSmaller(arrayOne)
    leftTwo = findSmaller(arrayTwo)
    rightOne = getBiggerOrEqual(arrayOne)
    rightTwo = getBiggerOrEqual(arrayTwo)

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)




def findSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def getBiggerOrEqual(array):
    larger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            larger.append(array[i])
    return larger

