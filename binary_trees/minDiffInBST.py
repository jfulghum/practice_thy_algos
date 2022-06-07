# https://leetcode.com/problems/minimum-distance-between-bst-nodes/submissions/

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans
