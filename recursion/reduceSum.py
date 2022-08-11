# // Given an array of length n, create an output value that is created by doing the following:
# // Create an array of length n-1 by summing all adjacent values.
# // Repeating step 1 until the array is of length 1.
# // For example, let's say the input is [1, 2, 3, 4, 5]. 
# // The next array would be [1 + 2, 2 + 3, 3 + 4, 4 + 5] which is [3, 5, 7, 9]
# // The next array would be [8, 12, 16]
# // The next array would be [20, 28]
# // The final array would be [48], so return 48.
# // Function Signature: 
# // function reduceSum(input)

# input: array [1, 2, 3, 4, 5]
# result integer 

# i =0
# while i > len(array)
#   result = recursive(array[i:])


#   
# recursive
# result = take adjacent sum:
# return result


# [1, 2, 3, 4, 5]
# [3, 5, 7, 9]

def reduceSum(input):
    if len(input) == 0:
        return None
    i = 0
    while i < len(input) - 1:
        input = helper(input)
    
    return input[0]


def helper(input):
    result = []
    for i in range(1, len(input)):
        result.append(input[i - 1] + input[i])
    return result

print(reduceSum([1, 2, 3, 4, 5]), 48) 

print(reduceSum([1, 2]), 3) 

print(reduceSum([]), None) 

print(reduceSum([1]), 1)
