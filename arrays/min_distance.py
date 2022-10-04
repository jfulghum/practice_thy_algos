"""
Given an array of numbers, return the minimum distance between any two numbers.

# Examples

-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

[3, 1, 5, 10, 6] => 1  # 5 and 6 are different by 1

[-2, -1, 4, 5] # 1 abs(-1 - -2) = 1 

distance = +Infinity

sort the array
traverse from idx 1 to last:
    distance = min(disntance, array[curr] - array[curr - 1]);

return distance === +Infinity ? -1 : distance

"""


def min_dist(array):

    if  not array or len(array) < 2:
        return -1

    array.sort()
    min_distance = float('inf')

    for i in range(1, len(array)):
        min_distance = min(min_distance, array[i] - array[i - 1])

    return min_distance


# includes gap over zero, and multiple same-distance pairs, and one really distant pair
# includes the shortest gap over zero  e.g., [-12, -1, 1, 300, 87184]
print(min_dist([-2, -1, 4, 5]), ' should be ', 1)

# null case (aka not an array)
print(min_dist(None), ' should be ', -1)

# empty array
print(min_dist([]), ' should be ', -1)

# length of 1
print(min_dist([1]), ' should be ', -1)
# 
