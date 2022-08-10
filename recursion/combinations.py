def solution(a):
    if len(a) == 0:
        return [[]]

    cs = []
    for c in solution(a[1:]):
        cs += [c, [a[0]]+c]
    return cs
    
nums= [1, 2, 3]
# Output:
# [[], 
#  [1], 
#  [2], 
#  [1,2], 
#  [3], 
#  [1,3], 
#  [2,3], 
#  [1,2,3]]

print(solution(nums))



# for every additional number, you double the output. 
# Space complexity is  2 O(n) 
# Time complexity is 2 O(n)



# Example 1

# getAllSubsequences("abc") == [
#   "a",
#   "b",
#   "c",
#   "ab",
#   "ac",
#   "bc",
#   "abc",
# ]

# THEN getAllSubsequences("abcd") == [
# You have all the letters you have before, and now you have to add another letter to EVERYthing you already had.

# Example 2:



#   "a",
#   "b",
#   "c",
#   "d",
#   "e",
#   "ab",
#   "ac",
#   "bc",
#   "abc",

#   "ad",
#   "bd",
#   "cd",
#   "abd",
#   "acd",
#   "bcd",
#   "abcd",



def helper(current, remaining, result):
    running_list = []
    for i in range(len(remaining)):
        new_current = current + remaining[i]
        helper(new_current, remaining[i+1:], result)
        result.append(new_current)

def getAllSubsequences(string):
    result = []

    helper("", list(string), result)
    
    return result

print(getAllSubsequences("abc"))
print(getAllSubsequences("abcd"))
print(getAllSubsequences(""))
print(getAllSubsequences("abcdef"))




# all possible -> think it's RECURSION
# it's always remove one element, and then recurse on the the remaining.

# think of interating thru all the substrings and recursing on the remaining. 
# (It's that structure for 'all possible' problems.)


# how to change so it's permutations?
def helper(current, remaining, result):
    if len(remaining) == 0:
        result.append(current)
    
    for i in range(len(remaining)):
        new_current = current + remaining[i]
        new_remaining = remaining.copy()
        new_remaining.pop(i)
        helper(new_current, new_remaining, result)

def getAllSubsequences(string):
    result = []

    helper("", list(string), result)
    
    return result

