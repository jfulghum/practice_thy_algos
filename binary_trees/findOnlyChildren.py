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
         
    helper(root.left)
    helper(root.right)
  
  helper(root)

  return single_child_nodes


print(findOnlyChildren(TreeNode(2, TreeNode(2), TreeNode(3, None, TreeNode(4)))) , [4])
print(findOnlyChildren(TreeNode(2, TreeNode(2, TreeNode(24), None), TreeNode(3, None, TreeNode(4)))), [24, 4])
# returns correctly 
# 
# [4] [4]
# [24, 4] [24, 4]


# remember! this doesn't work b/c of the
# dangers of having mutable objects as default parameters!
# https://docs.quantifiedcode.com/python-anti-patterns/correctness/mutable_default_value_as_argument.html

 def findOnlyChildren2(root, single_child_nodes = []):

    if not root:
        return None

    if not root.left is not None and root.right:
        single_child_nodes.append(root.right.value)

    if root.left and not root.right is not None:
        single_child_nodes.append(root.left.value)
            
    findOnlyChildren2(root.left)
    findOnlyChildren2(root.right)

    return single_child_nodes
  
  
 # Hi, why can you seem to access mutable objects in Python from outer scope but not immutable objects?
# You kind of answered your own question in the question,
# it's immutable.
# e.g. findOnlyChildren requires a helper, sumOnlyChildren does not.

def findOnlyChildren(root):

  single_child_nodes = []

  def helper(root):
    if not root:
      return

    if not root.left is not None and root.right:
      single_child_nodes.append(root.right.value)

    elif root.left and not root.right is not None:
      single_child_nodes.append(root.left.value)
         
    helper(root.left)
    helper(root.right)
  
  helper(root)

  return single_child_nodes

def sumOnlyChildren(root, sum=0):

  if not root:
    return

  if not root.left is not None and root.right:
    sum += root.right.value

  elif root.left and not root.right is not None:
    sum += root.left.value
       
  sumOnlyChildren(root.left, sum)
  sumOnlyChildren(root.right, sum)
  
  return sum

tree2 = TreeNode(2, TreeNode(2))

print(sumOnlyChildren(tree2)) # 4

