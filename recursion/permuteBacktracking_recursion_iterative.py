
# Given an array of N integers, generate all permutations of the given array.
# Function Signature: 
# get_permutations(l: List[int]) -> List[List[int]]
# Target runtime and space complexity:
# O(N!) time, O(N) space; N = length of input

# 1 2 3
# 2 1 3
# 2 3 1
# 3 2 1
# 3 1 2
# 1 3 2
# 1 2 3
# steps
# 1- swap every two elemnts untill u reach to the end
# 2- if u reached to the end of the arr, return to the begining
# 3- repeat (1, 2) steps untill u reach to the orginal arr again
# 1 2 3 4
# [4 3 2 1]

# Next permutation
# Given an array of objects a[] that represents a permutation, the next permutation can be found as follows:
# Let i be the greatest index where a[i] < a[i+1]
# Let j be the greatest index where a[j] > a[i]
# Swap a[i] and a[j]
# Reverse all elements from i+1 to the end of the array
# for example, if the array is 8 items long, and i = 3, then swap a[4] and a[7], and swap a[5] and a[6].

def permute(nums):
    numsOrg = nums.copy()
    while (True):
        # 1 2 3
        for i in range(len(nums)-1):
            # temp = nums[i]
            # nums[i] = nums[i+1]
            # nums[i+1] = temp
            nums[i+1], nums[i] = nums[i], nums[i+1]
            print(nums)

        if(nums == numsOrg):
            break

# permute([1, 2])
    
    

    # [ 1,2,3]

## new_array = [], 
# if len(new_array) == len(array):
    # print(new_array)
# for i in array:
#  if ele not in new_array
#    add ele to new_array
#    permuate(new_array, array)
#    new_array.pop()

array = [1,2,3]

def permuteBacktracking(array):
    new_array = []

    def helper(array):
        if len(new_array) == len(array):
            print(new_array)
            
        for ele in array:
            if ele not in new_array:
                new_array.append(ele)
                helper(array)
                new_array.pop()

    helper(array)

permuteBacktracking(array)
