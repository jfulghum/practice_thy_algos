
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

def averageOfLevelsStacks(root):
  if root is None:
    return root
  stack = [root]
  result = []
  while stack:
    Sum = 0
    count = 0
    temp = []
    while stack:
      n = stack.pop()
      Sum += n.value
      count += 1
      if (n.left != None):
        temp.append(n.left)
      if (n.right != None):
        temp.append(n.right)
    stack = temp
    result.append(Sum * 1.0 / count)
  return result


tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(9) )), TreeNode(3, TreeNode(6, TreeNode(7))))
#       1
#     /  \
#   2      3    #2.5
# /  \    /
# 4   5  6      # 5.0
  #  /  /
  # 9  7       #8.0
print("stack:")
print(arrayifyTree(tree))
print(averageOfLevelsStacks(tree)) # [1.0, 2.5, 5.0, 7.0]

# Importing Queue
from queue import Queue

def averageOfLevelsQueues(root):
  if root is None:
    return root
  q = Queue()
  q.put(root)
  result = []
  while (not q.empty()):
    Sum = 0
    count = 0
    temp = Queue()
    while (not q.empty()):
      n = q.queue[0]
      q.get()
      Sum += n.value
      count += 1
      if (n.left != None):
        temp.put(n.left)
      if (n.right != None):
        temp.put(n.right)
    q = temp
    result.append(Sum * 1.0 / count)
  return result

print("queue:")
print(arrayifyTree(tree))
print(averageOfLevelsQueues(tree)) # [1.0, 2.5, 5.0, 7.0]

