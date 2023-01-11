class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_dfs(root: TreeNode, target: int) -> bool:
    # Write your code here. 
    pass

# Test Cases
tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(find_dfs(None, 1), False)
print(find_dfs(tree1, 9), True)
print(find_dfs(tree1, 1), False)
print(find_dfs(tree1, 2), True)
print(find_dfs(TreeNode(1), 2), False)

# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# Iterative Solution
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
def find_dfs(node: TreeNode, target: int) -> int:
    if not node:
        return False

    stack = [node]    
    while stack:
        curr = stack.pop()
        if curr.value == target:
            return True
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
        
    return False

# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# ⬛️ Recursive Solution
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
def find_dfs_rec(node, target):
    if not node:
        return False

    if node.value == target:
        return True

    return find_dfs_rec(node.left, target) or find_dfs_rec(node.right, target)
