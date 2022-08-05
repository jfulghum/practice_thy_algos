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
