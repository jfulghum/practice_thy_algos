# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/submissions/

# Given a binary array data, return the minimum number of swaps 
# required to group all 1’s present in the array together in any place in the array.
# Example 1:

# Input: data = [1,0,1,0,1]
# Output: 1
# Explanation: There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap.
# [0,1,1,1,0] using 2 swaps.
# [0,0,1,1,1] using 1 swap.
# The minimum is 1.
# Example 2:

# Input: data = [0,0,0,1,0]
# Output: 0
# Explanation: Since there is only one 1 in the array, no swaps are needed.
# Example 3:

# Input: data = [1,0,1,0,1,0,0,1,1,0,1]
# Output: 3
# Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # want to find a sub array with the smallest number of 0s possible.
        
        # find how many 1s there are, that's the window size.
        window_size = 0
        for num in data:
            if num == 1:
                window_size += 1
        maxOnesInWindow = 0
        ones_in_window = 0
        for i in range(len(data)):
            ones_in_window += data[i]
            if i >= window_size:
                ones_in_window -= data[i - window_size]
            maxOnesInWindow = max(ones_in_window, maxOnesInWindow)
            
        return window_size - maxOnesInWindow
            
