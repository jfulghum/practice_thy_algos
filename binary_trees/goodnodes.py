# https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, max_so_far):
            nonlocal num_good_nodes
            if max_so_far <= node.val:
                num_good_nodes += 1
            
            if node.right:
                helper(node.right, max(node.val, max_so_far))
            if node.left:
                helper(node.left, max(node.val, max_so_far))

        num_good_nodes = 0
            
        helper(root, float('-inf'))
        
        return num_good_nodes
