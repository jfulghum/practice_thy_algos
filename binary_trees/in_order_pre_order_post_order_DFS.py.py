def inOrderTraversal(root):
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.value)
            else:  
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return res


# note these are ALL DFS (you can tell b/c they are all recursive)
# note if it's a BST/valid Binary Search Tree, inOrder will produce a list of lowest to highest values

#recursive
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array
