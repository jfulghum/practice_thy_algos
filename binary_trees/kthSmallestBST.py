# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/


# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def kthSmallest(t, k):
    n = 0
    stack = []
    cur = t
    
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left 
        
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.value
        cur = cur.right

