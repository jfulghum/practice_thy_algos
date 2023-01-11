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





# left, then right. to remember:
# left check, right cheek, left cheek, right cheek, it must be a crime to be as fine as you
# booty wurk booty wurk, lemme see that booty wurk



# If it's a graph instead of a tree (it's the same but even easier b/c you don't need to call left and right separately) :

def dfs(node):
  # Base Case
  if not node: return
  # Preorder operation
  print(node.val)
  # Recursive case
  for next_node in node.neighbors:
    dfs(next_node)
    
    
    
# if there is a loop
def loop_safe_dfs(node, visited):
  # Base Case
  if not node: return
  if node in visited: return # <<<<<
  # Preorder operation
  visited.add(node) # <<<<<<
  print(node.val)
  # Recursive case
  for next_node in node.neighbors:
    dfs(next_node, visited)
