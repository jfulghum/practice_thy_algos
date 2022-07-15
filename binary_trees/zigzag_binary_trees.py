# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     3 
#   9   20
#      15  7

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        queue = collections.deque([root])
        output = []
        left = True
        currentLevel = 0
        while queue:
            output.append(collections.deque())
            levelLength = len(queue)
            for i in range(levelLength):
                currentNode = queue.popleft()
                if left:
                    output[currentLevel].append(currentNode.val)
                else:
                    output[currentLevel].appendleft(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
         
            currentLevel += 1
            left = not left
        return output
        
