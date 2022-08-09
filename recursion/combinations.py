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
