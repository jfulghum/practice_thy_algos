"""

Given a N-ary tree

return a collection of linked lists, where eacr list contains the elements of one level in the tree


       1 
     / | \
     2 3 4
       | |
       5 6 

=> [
    1 -> None,
    2 -> 3 -> 4 -> None,
    5 -> 6 -> None
]
"""
class Node:
    value: int
    children: List['Node']


'''
sudo code:

[2,3,4,5,6]
3
while(size)
    2children to the que
    size--

create queue to do BFS

at each level take the size of the queue to limit the amount of items in queue to a level and push items in an array to result array

iterate through result array and create linked lists for each level


'''

from collections import deque

class LLNode:

    def __init__(self,val,next= None):
        self.val = val
        self.next = next



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
    

'''
       1 
     / | \
     2 3 4
       | |
       5 6 
'''
