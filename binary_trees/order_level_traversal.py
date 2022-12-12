# level order traversal 

def solution(root):
    levels = []
    if not root:
        return levels
    
    def helper(node, level):
        if len(levels) == level:
            levels.append([])

        levels[level].append(node.value)

        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)
        
    helper(root, 0)
    return levels
