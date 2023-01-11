class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# isValidBST, create helper function with min value & max value


def isValidBST(node: Node) -> bool:
  def valid(node, minValue, maxValue):
    if node is None:
      return True
      
    if node.value < minValue or node.value > maxValue:
      return False

    return valid(node.left, minValue, node.value) and valid(node.right, node.value, maxValue)

  return valid(node, float('-inf'), float('inf'))
      

print(isValidBST(None))
print(isValidBST(Node(5)))

#   5
# 1
print(isValidBST(Node(5, Node(1))))

#   5
# 10
print(isValidBST(Node(5, Node(10))) == False)

#  5
#   10
print(isValidBST(Node(5, right=Node(10))))

#  5
#   1
print(isValidBST(Node(5, right=Node(1))) == False)

#   5
# 1  10
print(isValidBST(Node(5, Node(1), Node(10))))

#   5
# 10  1
print(isValidBST(Node(5, Node(10), Node(1))) == False)

#      10
#   5      15
# 3   7 12   17
root = Node(
  10,
  Node(5,
    Node(3), Node(7)),
  Node(15,
    Node(12), Node(17)))
print(isValidBST(root))

#       10
#   5      15
# 2   16 3   20
root = Node(
  10,
  Node(5,
    Node(2), Node(16)),
  Node(10,
    Node(3), Node(20)))
print(isValidBST(root) == False)

#       10
#   15     20
# 30  40  1  12
root = Node(
  10,
  Node(15,
    Node(30), Node(40)),
  Node(20,
    Node(1), Node(12)))
print(isValidBST(root) == False)

#   10
# 1    20
#  4 15
root = Node(
  10,
  Node(1,
    right=Node(4)),
  Node(20,
    Node(15)))
print(isValidBST(root))

#   10
# 1    20
#  99 99
root = Node(
  10,
  Node(1,
    right=Node(99)),
  Node(20,
    Node(99)))
print(isValidBST(root) == False)

# # Test Cases
# tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
# print(find_dfs(None, 1), False)
# print(find_dfs(tree1, 9), True)
# print(find_dfs(tree1, 1), False)
# print(find_dfs(tree1, 2), True)
# print(find_dfs(TreeNode(1), 2), False)
