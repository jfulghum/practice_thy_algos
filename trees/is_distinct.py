# A binary tree is immediately distinct if no root node in the tree has a child node with the same value.
# Given the root of a binary tree, return true if the given tree is immediately distinct, or false otherwise.
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def is_distinct(node: TreeNode) -> int:
  if not node:
    return False
  stack = [node]
  while stack:
    curr = stack.pop()
    if (curr.left and curr.value == curr.left.value) or (curr.right and curr.value == curr.right.value):
      return False
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)
    
  return True
  
print(is_distinct(None), False)
print(is_distinct(TreeNode(2, TreeNode(2), TreeNode(3))), False)
print(is_distinct(TreeNode(2, TreeNode(29, TreeNode(29)), TreeNode(4, TreeNode(2, TreeNode(9))))), False)
print(is_distinct(TreeNode(8, TreeNode(8))), False)
print(is_distinct(TreeNode(7, TreeNode(8))), True)
print(is_distinct(TreeNode(7, TreeNode(8), TreeNode(9))), True)
