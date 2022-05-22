class BTNode:
  def __init__(self, value = 0, left = None, right = None):
      self.value = value
      self.left = left
      self.right = right

class TreeNode:
  def __init__(self, value = 0, left = None, right = None):
      self.value = value
      self.left = left
      self.right = right

def sum_tree(root: TreeNode) -> int:
  if root is None:
    return 0
  sum = 0
  stack = [root]
  while stack:
    curr = stack.pop()
    sum += curr.value
    if curr.left:
      stack.append(curr.left)
    if curr.right:
      stack.append(curr.right)
  return sum

# Test Cases
print(sum_tree(None), 0)
print(sum_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 6)
print(sum_tree(TreeNode(1)), 1)
print(sum_tree(TreeNode(1, TreeNode(3), TreeNode(3))), 7)
