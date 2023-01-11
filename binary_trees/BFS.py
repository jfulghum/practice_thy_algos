# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# ⬛️ Iterative Solution
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

from collections import deque
def find_bfs(node: TreeNode, target: int) -> bool:
    if not node:
        return False

    queue = deque([node]) # We use a deque so we can pop the leftmost element in O(1)
    while queue:
        curr = queue.popleft()
        if curr.value == target:
            return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        
    return False


# left, then right. to remember:
# left check, right cheek, left cheek, right cheek, it must be a crime to be as fine as you
# booty wurk booty wurk, lemme see that booty wurk



# If it's a graph instead of a tree (it's the same but even easier b/c you don't need to call left and right separately) :

from collections import deque

def bfs(node):
  queue = deque()
  queue.append(node)
  while len(queue) > 0:
    node = queue.popleft()
    print(node.val)
    for n in node.neighbors:
      queue.append(n)
    
# If it's a graph with a cycle, add a visited set: 
from collections import deque

def bfs(node):
  queue = deque()
  visited = set() # <<<<
  queue.append(node)
  visited.add(node) # <<<<
  while len(queue) > 0:
    node = queue.popleft()
    print(node.val)
    for n in node.neighbors:
      if n not in visited: # <<<<
        queue.append(n) 
