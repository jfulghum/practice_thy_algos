def findDirectReport(root, a, b):
  if root is None:
    return root
  stack = [root]
  children = []
  while stack:
    curr = stack.pop()
    if curr.left:
      children.append(curr.left.value)
      stack.append(curr.left)
    if curr.right:
      children.append(curr.right.value)
      stack.append(curr.right)
    if curr.value == a and b in children:
      return True
    children = []
  return False
  

  
  
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(9) )), TreeNode(3, TreeNode(6, TreeNode(7))))
#       1
#     /  \
#   2      3    #2.5
# /  \    /
# 4   5  6      # 5.0
  #  /  /
  # 9  7       #8.0




# print(arrayifyTree(tree))
print(findDirectReport(tree, 1, 2)) # True
print(findDirectReport(tree, 2, 9)) # False
print(findDirectReport(tree, 3, 7)) # False
