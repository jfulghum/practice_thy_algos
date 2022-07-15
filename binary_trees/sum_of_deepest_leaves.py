# https://leetcode.com/problems/deepest-leaves-sum/solution/


# remember, sum of deepest LEAVES not the sum of the longest path or something else. spend SO MUCH time understanding what the problem is asking.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        next_level = deque([root,])
        
        while next_level:
            curr_level = next_level
            test = [x.val for x in curr_level]
            next_level = deque()
            
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return sum([node.val for node in curr_level])
