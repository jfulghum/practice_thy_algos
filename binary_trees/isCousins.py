# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = collections.deque([root])
        
        while queue: 
            
            cousins = False 
            siblings = False
            
            length = len(queue)
            
            for _ in range(length):
                
                node = queue.popleft()
                
                if node is None:
                    siblings = False
                else:
                    if node.val == x or node.val == y:
                        
                        if not cousins:
                            siblings = True
                            cousins = True
                        else:
                            return not siblings
                        
                    queue.append(node.left) if node.left else None
                    queue.append(node.right) if node.right else None
                    
                    queue.append(None)
                
            if cousins:
                return False
            
        return False
