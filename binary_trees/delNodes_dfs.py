class Solution:
     def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, is_root):
            if not node:
                return
            
            is_node_deleted = node.val in to_delete
            if is_root and not is_node_deleted:
                result.append(node)
                
            node.left = dfs(node.left, is_node_deleted)
            node.right = dfs(node.right, is_node_deleted)
            
            return node if not is_node_deleted else None
            
        
        result = []
        to_delete = set(to_delete)
        dfs(root, True)

        return result
