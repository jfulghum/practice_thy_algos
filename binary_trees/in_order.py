def inOrderTraversal(root):
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.value)
            else:  # inorder: left -> root -> right
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return res
