class BTNode:
  def __init__(self, value = 0, left = None, right = None):
      self.value = value
      self.left = left
      self.right = right
    
def arrayifyTree(root):
    if root is None:
        return []
    queue = []
    array = []
    queue.append(root)
    while (len(queue) != 0):
        node = queue.pop(0)
        array.append(node.value)
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
    return array
  
class TreeNode:
  def __init__(self, value = 0, left = None, right = None):
      self.value = value
      self.left = left
      self.right = right

# DFS through the tree using a helper function, passing down the parent node at each step and modifying the current node value.
# Return the original root node of the modified tree.

def parent_sum_tree(node):
  if not node:
    return node

  stack = [node]    
  while stack:
    curr = stack.pop()
    if curr.left:
      stack.append(curr.left)
      curr.left.value = curr.left.value + curr.value
    if curr.right:
      stack.append(curr.right)
      curr.right.value = curr.right.value + curr.value
      
  return node

# Test Cases
print(arrayifyTree(parent_sum_tree(None))) # []
print(arrayifyTree(parent_sum_tree(TreeNode(1, TreeNode(2), TreeNode(3))))) # [1, 3, 4]
print(arrayifyTree(parent_sum_tree(TreeNode(1)))) # [1]
print(arrayifyTree(parent_sum_tree(TreeNode(1, TreeNode(3), TreeNode(3, TreeNode(6)))))) # [1, 4, 4, 10]
