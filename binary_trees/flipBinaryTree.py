class BTNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def arrayifyTree(root):
    if root is None:
        return []
    queue = []
    array = []
    queue.append(root)
    while (len(queue) != 0):
        node = queue.pop(0)
        array.append(node.value)
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
    return array


def flipBinaryTree(root: BTNode):
    stack = [root]
    while stack:
        node = stack.pop(-1)
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root


tree1 = BTNode(1,
  BTNode(2,
    BTNode(4),
    BTNode(5),
  ),
  BTNode(3,
    BTNode(6),
    BTNode(7),
  ),
);

print(arrayifyTree(tree1))
print(arrayifyTree(flipBinaryTree(tree1)));
