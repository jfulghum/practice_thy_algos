#https://leetcode.com/problems/binary-tree-paths/solution/



# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def solution(t):
    if t is None:
        return []
    paths = []
    stack = [(t, str(t.value))]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.right:
            stack.append((node.right, path + '->' + str(node.right.value)))
        if node.left:
            stack.append((node.left, path + '->' + str(node.left.value)))
    return paths
