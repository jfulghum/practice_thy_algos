
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

array = [6,5,4,3,2,1] # [1, 1, 1, 1, 1, 0]

array = [1,2,3,4,5,6] # [1, 1, 1, 1, 1, 0]

array = [5,4,3,4] # [2, 2, 1, 0]

array = [5,4,3,4,17] # [3, 2, 1, 1, 0]

class Solution:
  def canSeePersonsCount(self, heights):
    n = len(heights)
    res = [0 for _ in range(n)]
    stack = []
    for i in range(n - 1, -1, -1):

        while stack and heights[i] > stack[-1]:

          stack.pop()
          res[i] += 1
        res[i] += 1 if stack else 0
        stack.append(heights[i])
    return res


print(Solution().canSeePersonsCount(array))

# There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

# A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

# Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

 

# Example 1:



# Input: heights = [10,6,8,5,11,9]
# Output: [3,1,2,1,1,0]
# Explanation:
# Person 0 can see person 1, 2, and 4.
# Person 1 can see person 2.
# Person 2 can see person 3 and 4.
# Person 3 can see person 4.
# Person 4 can see person 5.
# Person 5 can see no one since nobody is to the right of them.
