def sumNodesWithEvenParentRecursively(root):
  if not root:
    return

  sum = 0

  if (root.value % 2 == 0):
    if (root.left):
      sum += root.left.value

    if (root.right):
      sum += root.right.value

  if (root.left):
    sum += sumNodesWithEvenParentRecursively(root.left)
  if (root.right):
    sum += sumNodesWithEvenParentRecursively(root.right)
  
  return sum

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(9) )), TreeNode(3, TreeNode(6, TreeNode(7))))

print(sumNodesWithEvenParentRecursively(tree))



def sumNodesWithEvenParentStack(root):
  if root is None:
    return root
  sum = 0
  stack = [root]
  while stack:
    curr = stack.pop()
    if curr.value % 2 == 0:
      if curr.left:
        sum += curr.left.value
      if curr.right:
        sum += curr.right.value
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)
  return sum 


tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(9) )), TreeNode(3, TreeNode(6, TreeNode(7))))
#       1
#     /  \
#   2      3   
# /  \    /
# 4   5  6     
#    /  /
#   9  7      


print(sumNodesWithEvenParentRecursively(tree)) # 16
print(sumNodesWithEvenParentStack(tree)) # 16


