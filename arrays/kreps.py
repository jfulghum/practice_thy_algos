'''

The original solution, using a dictionary to keep track of the number of repetitions. Early return when you find an element that hits k.

The original solution, but do not return early. Build up the full dictionary of counts. Iterate through the array again and return the first one whose count is greater than or equal k. Discuss how this does not change the overall runtime or space complexity.

For each element, iterate through the rest of the array to see if it is repeated k times. If it is, return it. Otherwise, go onto the next element. Walk through how this approach is O(n^2) runtime.

given an array of integers and a integer k, return the first element to k occurences

([3,4,5,5,5,6,6,6] , 3) # 5

'''

def kreps(arr, k):
    counts = {}
    for elem in arr:
        counts[elem] = counts.get(elem, 0) + 1
        if counts[elem] == k:
            return elem
    return None

def kreps2(arr, k):
    counts = {}
    for elem in arr:
        counts[elem] = counts.get(elem, 0) + 1
    for elem in arr:
        if counts[elem] == k:
            return elem
    return None
    
 # Space complexity doesn’t change. 

# Compared to before, the worst case is the same.

# [1,1,2,2,2,1], k =3
# 2
# 1

print(kreps([3,4,5,5,5,6,6,6], 3), 'expect 5')
print(kreps([1,2,3], 1), 'expect 1')
print(kreps([], 1), 'expect None')
