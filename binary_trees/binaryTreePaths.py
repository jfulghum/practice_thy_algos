# https://leetcode.com/problems/binary-tree-paths/submissions/class Solution:

#iteratively 

def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    if root is None:
        return root
    paths = []
    stack = [(root, str(root.val))]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.left:
            stack.append((node.left, path + "->" + str(node.left.val)))

        if node.right:
            stack.append((node.right, path + "->" + str(node.right.val)))
    return paths

#recursively
  class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(node, path):
            
            if not node.left and not node.right:
                paths.append(path)
                
            if node.left:
                dfs(node.left, path + "->" + str(node.left.val))
                
            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))
                
        paths = []
        dfs(root, str(root.val))
        
        return paths
