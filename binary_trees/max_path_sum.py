"""
AGENDA

1) Max path sum
2) LCA
3) Trie/Word Search
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Note: you would use nonlocal variable if you are in a solution class

global_max = float('-inf')
def max_path_sum(root):
    global global_max
    # base case
    if not root: return 0

    # get left and right maxes
    left_branch_max = max_path_sum(root.left)
    right_branch_max = max_path_sum(root.right)

    # check if our current root is the middle of the longest path
    global_max = max(global_max, root.val + left_branch_max + right_branch_max)


    # return the current value + max(left, right)
    max_current_path = root.val + max(left_branch_max, right_branch_max)
    return max(0, max_current_path)


tree = TreeNode(1,
            TreeNode(2),
            TreeNode(3,
                TreeNode(-5),
                TreeNode(-4),
            )
)

max_path_sum(tree)
print(global_max) # 6


