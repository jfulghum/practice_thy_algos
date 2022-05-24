
class TreeNode:
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

def prune(root, x):
  if root is None:
    return root
  if root.value == x:
    root = None
  if root and root.right:
    root.right = prune(root.right, x)
  if root and root.left:
    root.left = prune(root.left, x)
  return root 


tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(9) )), TreeNode(3, TreeNode(6, TreeNode(7))))
#       1
#     /  \
#   2      3   
# /  \    /
# 4   5  6     
#    /  /
#   9  7      

print(arrayifyTree(tree))
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(9) )), TreeNode(3, TreeNode(6, TreeNode(7))))

print(arrayifyTree(prune(tree, 3))) # correctly returns [1, 2, 4, 5, 9]

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(9) )), TreeNode(3, TreeNode(6, TreeNode(7))))

print(arrayifyTree(prune(tree, 6))) # [1, 2, 3, 4, 5, 9]
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(9) )), TreeNode(3, TreeNode(6, TreeNode(7))))

print(arrayifyTree(prune(tree, 1))) # []

tree = TreeNode(1, TreeNode(3, TreeNode(4), TreeNode(5, TreeNode(9) )), TreeNode(3, TreeNode(6, TreeNode(7))))

#       1
#     /  \
#   3      3   
# /  \    /
# 4   5  6     
#    /  /
#   9  7 

print(arrayifyTree(prune(tree, 3))) # [1]
