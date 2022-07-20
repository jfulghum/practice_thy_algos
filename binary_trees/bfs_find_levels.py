'''
Given a binary tree (NOT a BST), find a target element using Breadth First Search.

'''

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def printNode(node):
    print(node.value)
    if node.left:
        printNode(node.left)
    if node.right:
        printNode(node.right)



# return True if target is found
# return False if target is not found if no node False

#test cases 
# no node at all, multiple nodes of same target node, no target node, root is target, target is furthest from root

# if root is None return Flase
# initalize q
# while q 
# if curr is target, return True
# add the children to queue
# return False

from collections import deque

# def find_bfs(root):
#     if root is None:
#         return False
    
#     queue = deque([root])
#     while queue:
#         temp = queue.copy()
#         node = queue.popleft()
#         print(node.value)
#         while temp:
#             node = temp.popleft()
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         temp = []
        

def find_bfs(root):
    if root is None:
        return False
    level = 0
    queue = deque([(root, level)])
    values = {}
    counts = {}
    while queue:
        node, level = queue.popleft()
        print(node.value, level)
        values[level] = values.get(level, 0) + node.value
        counts[level] = counts.get(level, 0) + 1
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1))
        level += 1
    result = []
    for key in values:
        result.append(values[key] / counts[key])
    print(result)


            

#      3
#   29      4
# 2        5 
#         9


tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(5, TreeNode(9))))

find_bfs(tree1)

# take a binary return the average of the levels 

#      1.    # 1
#   2.   3   # 2.5 
# 4.  5  6 7  #  5.5 

# [1, 2.5, 5.5]

# bfs queue interate
# levels = [root.val] 
# queue = [root]
# while queue
# initalize queue, sum = 0, count = 0, level = []
# 
# temp = queue
# while temp:
# curr = temp.pop()
# put curr children in queue
# add sum, add count 

#
# levels.append(level)
# level = []


tree1 = TreeNode(1)
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))


