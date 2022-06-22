# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q 
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


#lowest like the lowest LEVEL (it's not referring to the node's value)
#Note: a node can be an Ancestor of itself - or at least ask that as a clarification

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node, p, q):
            if node is None:
                return None

            if node == p or node == q:
                return node

            left = helper(node.left, p, q)
            right = helper(node.right, p, q)
            
            if left and right:
                return node
            
            if left is None and right is None:
                return None 
            
            return left or right
#             if left:
#                 return left
#             if right:
#                 return right
        
        return helper(root, p, q)
