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
        
def count_tree(root: TreeNode) -> int:
  if root is None:
    return 0
  count = 0
  stack = [root]
  while stack:
    curr = stack.pop()
    count += 1
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)
  return count

#recursive
def count_tree_rec(node):
    if not node:
        return 0
    return 1 + count_tree_rec(node.left) + count_tree_rec(node.right)

# Test Cases
print(count_tree(None), 0)
print(count_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 3)
print(count_tree(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 6)
print(count_tree(TreeNode()), 1)
