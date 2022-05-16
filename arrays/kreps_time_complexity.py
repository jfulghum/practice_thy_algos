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

# Time is O(n) and Space is o(n) 
    # You call “linear” b/c it scales linearly with the scale of the input.


def kreps2(arr, k):
    counts = {}
    for elem in arr:
        counts[elem] = counts.get(elem, 0) + 1
    for elem in arr:
        if counts[elem] == k:
            return elem
    return None

# Time complexity ^^ doesn't change b/c:
#      Compared to before, the worst case is the same.
# Space complexity doesn’t change. it is O(n).


def kreps3(arr, k):
    for i in range(len(arr)):
        count = 0
        for j in range(i, len(arr)):
            if arr[j] == arr[i]:
                count += 1
            if count == k:
                return arr[i]
    return None

# Time complexity is N^2. 
    # You are doing N operations N times. 
# Space complexity here is better b/c Space is constant.
    # Space is not constant NOT b/c we aren't creating anything that requires space, we are, count requires space, but nothing that requires N space. 



# [1,1,2,2,2,1], k =3
# 2
# 1

print(kreps3([3,4,5,5,5,6,6,6], 3), 'expect 5')
print(kreps3([1,2,3], 1), 'expect 1')
print(kreps3([], 1), 'expect None')
    

# [1,1,2,2,2,1], k =3
# 2
# 1

print(kreps([3,4,5,5,5,6,6,6], 3), 'expect 5')
print(kreps([1,2,3], 1), 'expect 1')
print(kreps([], 1), 'expect None')
