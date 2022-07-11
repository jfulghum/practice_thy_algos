
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root):
        self.res = {}
        self.dfs(root, 0)
        return self.res.values()
        
    def dfs(self, node, depth):
        if not node:
            return 
        if depth not in self.res:
            self.res[depth] = node.val
        else:
            self.res[depth] = max(self.res[depth], node.val)
            
        self.dfs(node.left, depth + 1)
        
        self.dfs(node.right, depth + 1)



# Input: root = [1,2,3]
# Output: [1,3]


tree1 = TreeNode(1, TreeNode(2), TreeNode(3))



print(Solution().largestValues(tree1))
