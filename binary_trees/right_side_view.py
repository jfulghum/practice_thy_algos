from collections import deque 

def right_side_view(root):
    if root is None:
        return []
    next_level = deque([root,])
    
    result = []
    
    while (len(next_level)):
        curr_level = next_level
        next_level = deque()
        
        while curr_level:
            node = curr_level.popleft()
            if (node.left != None) :
                next_level.append(node.left)
 
            if (node.right != None) :
                next_level.append(node.right)
        result.append(node.value)
        
    return result
