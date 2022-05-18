class TreeNode:
  def __init__(self, value = 0, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right



def findOnlyChildren(root):

  single_child_nodes = []

  def helper(root):
    if not root:
      return

    if not root.left is not None and root.right:
      single_child_nodes.append(root.right.value)

    elif root.left and not root.right is not None:
      single_child_nodes.append(root.left.value)
         
    # Traversing the left child
    helper(root.left)
     
    # Traversing the right child
    helper(root.right)
  
  helper(root)

  # print(single_child_nodes) 
  return single_child_nodes


print(findOnlyChildren(TreeNode(2, TreeNode(2), TreeNode(3, None, TreeNode(4)))) , [4])
print(findOnlyChildren(TreeNode(2, TreeNode(2, TreeNode(24), None), TreeNode(3, None, TreeNode(4)))), [24, 4])
