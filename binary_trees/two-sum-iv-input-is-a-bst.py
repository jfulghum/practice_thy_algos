# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solution/

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # x + y = k
        # y = k - x
        l = set()
        
        def dfs(node):
            if not node: return False
            y = k - node.val
            if y in l:
                return True
            else:
                l.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
