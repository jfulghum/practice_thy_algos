def solution(array):
    if array is None:
        return None
    flip = True
    root = Tree(array[0])
    node = root
    for i in range(1, len(array)):
        if flip:
            node.right = Tree(array[i])
            node = node.right
            flip = False
        else:
            node.left = Tree(array[i])
            node = node.left 
            flip = True
    return root
        
