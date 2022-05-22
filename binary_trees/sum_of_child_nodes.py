# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root):
    if root is None:
        return root
    stack = [root]
    while stack:
        curr = stack.pop()
        sum = 0
        if curr.right:
            sum += curr.right.value
            stack.append(curr.right)
        if curr.left:
            sum += curr.left.value
            stack.append(curr.left)
        if sum != 0:
            curr.value = sum
    return root
