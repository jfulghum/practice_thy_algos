class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def arrayifyTree(root: TreeNode):
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

# Approach
# Have curr node that starts at the root of the tree. If the node is less than the target, move curr to curr.right. If the node is greater, move curr to curr.left. If the position that you're moving curr into is nil at any point, insert the node in that position instead of moving curr.

def insert_bst(root: TreeNode, target: int) -> TreeNode:
  if not root:
    return TreeNode(target)
  curr = root
  while curr:
    if curr.value < target:
      if curr.right:
        curr = curr.right
      else:
        curr.right = TreeNode(target)
        return root
    else:
        if curr.left:
          curr = curr.left
        else:
          curr.left = TreeNode(target)
          return root
    

# Test Cases
tree = TreeNode(6, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8))
print(arrayifyTree(insert_bst(tree, 7))) # [6, 3, 8, 2, 4, 7]
print(arrayifyTree(insert_bst(tree, 5))) # [6, 3, 8, 2, 4, 7, 5]
print(arrayifyTree(insert_bst(tree, 1))) # [6, 3, 8, 2, 4, 7, 1, 5]
print(arrayifyTree(insert_bst(None, 1))) # [1]

# Given tree:
#              6
#            /   \
#           3     8
#          / \    /
#         2   4  7
#        /     \
#       1       5
