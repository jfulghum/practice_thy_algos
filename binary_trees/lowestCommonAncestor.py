# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#lowest like the lowest LEVEL (it's not referring to the node's value)

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
