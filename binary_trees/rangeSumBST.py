# https://leetcode.com/problems/range-sum-of-bst

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return root
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if node:
                
                if low <= node.val <= high:
                    ans+= node.val
                
                if low < node.val:
                    stack.append(node.left)
                    
                if node.val < high:
                    stack.append(node.right)
                    
                    
        return ans
      
      
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal ans
            if node:
                if low <= node.val <= high:
                    ans += node.val
                dfs(node.left)
                dfs(node.right)
            
        ans = 0
        dfs(root)
        return ans
