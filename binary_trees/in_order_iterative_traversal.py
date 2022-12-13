#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def solution(root):
    current = root
    stack = [] 
    result = []
    while True:

        if current is not None:
            stack.append(current)
            current = current.left

        elif(stack):
            current = stack.pop()
            result.append(current.value) 
            current = current.right
 
        else:
            break
    

    return result
