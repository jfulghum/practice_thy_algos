from collection import deque 


def bfs(root):
    if not root:
        return None 

    queue = deque([root])
    result = [] 
    while queue:
        size = len(queue)
        currentLevel = []
        for _ in range(size):
            curr = queue.popleft()
            currentLevel.append(curr)
            for child in curr.children:
                queue.append(child)

        # make LL
        head = LLNode(-1)
        ptr = head
                
        for node in currentLevel: 
            ptr.next = LLNode(node)
            ptr=ptr.next
       
        result.append(head.next)    
    return result
