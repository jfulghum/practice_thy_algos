"""
Problem
Given a nested array where each element may be 1) an integer or 2) an array, whose elements themselves may be integers or further arrays, count the total number of arrays.
What is the shape or pattern of this nested array structure? There can be empty lists but never None/null.
Function Signature: 
def countArrays(nestedList: list) -> int:
Target runtime and space complexity:
Time: O(n), where n is the total elements in the nested array
Space: O(d), where d is the depth of the deepest nesting, since a stack frame is needed for each recursive call.
Examples:

Must be done recur 
print(countArrays([1, 2, 3]) == 1)
print(countArrays([1, [1, 2, 3], 3]) == 2)
print(countArrays([1, [1, [1, [1, [1]]]]]) == 5)
print(countArrays([]) == 1)

Approaches
[0, [], 1, [1, 2], [3, [4]]] -> 5

# Base case 
A = [1, 2, 3]
i = 0
progress to basecase i++

also 

simple for loop e


# Recur case 
if e is an arr: recur call 
else continue 



tot = 1
for ele in array:
    if type ele is array:
        return 1 + helper(ele)
return tot 



"""
def countArrays(nestedList: list):
    if nestedList is None:
        return 0

    tot = 1
    def helper(nestedList):
        nonlocal tot
        # base case 
        if type(nestedList) != list: 
            tot -= 1
            return 

        # recur case
        for ele in nestedList:
            if type(ele) == list:
                tot += 1
                helper(ele)
        return 
   
    helper(nestedList)
    return tot  

"""
Stack frame1: countArrays([3])
sumTotal = 1
for each  [3]

return 1
    
---------------------
Stack frame0: countArrays([1, 2, [3]])
sumTotal = 2
for each  [1, 2, [3]]
    element = [3]
    ---> sumTotal += 1
return sumTotal (2)


# when we return from the stack frame, we destroy it. we destroy that stack frame, and only have what was returned back.
that's why in python you can't have memory leaks, b/c it throws it away for you.

#charles 
"""
def countArrays(array: list) -> int:
    sumTotal = 1 # always count itself

    for element in array:
        if type(element) is list:
            sumTotal += countArrays(element)

    return sumTotal


print(countArrays([1, 2, 3]) == 1)
print(countArrays([1, [1, 2, 3], 3]) == 2)
print(countArrays([1, 2, 3]) == 1)
print(countArrays([1, [1, 2, 3], 3]) == 2)
print(countArrays([1, [1, [1, [1, [1]]]]]) == 5)
print(countArrays([1, [2,2], [3,3], [4,4], 5]) == 4)
print(countArrays([1, [2, [], 2], [3,[6],3], [4,4], 5]) == 6)
print(countArrays([[[[[[[[[[[[[]]]]]]]]]]]]]) == 13)
print(countArrays([]) == 1)
print(countArrays([[]]) == 2)
print(countArrays([[],[],[]]) == 4)
print(countArrays(None) == 0)
print(countArrays(1) == 0)
