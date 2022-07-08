# Sum Nodes With Odd Valued Parent

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def countOddParents(node):
    if node is None:
        return node

    stack = [node]

    result = 0 

    while stack:
        curr = stack.pop()
        if curr:
            if curr.value % 2 != 0 and curr.left:
                result += curr.left.value
            if curr.value % 2 != 0 and curr.right:
                result += curr.right.value

            stack.append(curr.left)
            stack.append(curr.right)

    return result 


tree1 = TreeNode(1, TreeNode(3, TreeNode(1), TreeNode(3, TreeNode(5))))
tree2 = TreeNode(1)
tree3 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4))))

print(countOddParents(tree1))
print(countOddParents(tree2))
print(countOddParents(tree3))
