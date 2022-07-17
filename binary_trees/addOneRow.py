# https://leetcode.com/problems/add-one-row-to-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int):
        def dfs(node, val, depth, d):
            if node is None:
                return
            if d+1 == depth:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
                return
            
            dfs(node.left, val, depth, d+1)
            dfs(node.right, val, depth, d+1)
        
        if depth==1:
            return TreeNode(val, root, None)
        
        d = 1
        dfs(root, val, depth, d)
        return root
