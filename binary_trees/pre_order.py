def solution(root):
    result = []
    def preorder(root):
        if root:
            result.append(root.value)
            preorder(root.left)
            preorder(root.right)
    
    preorder(root)
    return result
