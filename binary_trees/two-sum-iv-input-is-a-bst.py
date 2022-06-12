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

 
#this is better b/c it uses that the Tree is sorted.
class Solution:        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root, result):
            if (root is None):
                return False
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)

        result = []
        inorder(root, result)
        l = 0
        r = len(result) - 1
        while (l < r):
            sum = result[l] + result[r]
            if (sum == k):
                return True;
            if (sum < k):
                l += 1
            else:
                r -= 1
        return False
    
