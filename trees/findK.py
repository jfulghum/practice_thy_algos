# Given a binary tree and an integer (k), find and return an array of unique nodes that occur (k) times in the tree.
# For example, if Node(5) occurs 3 times in the tree, and (k) = 3, your result array would include Node(5).


'''
        5
    3       2
  3   2

k = 2 => [3, 2]

'''

class TreeNode:
  def __init__(self, value = 0, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right



from collections import deque

def findK(node, k):
    if node is None:
        return []

    queue = deque([node])
    counts = {}

    while queue:
        currNode = queue.popleft()
        new_count = counts.get(currNode.value, 0) + 1
        counts[currNode.value] = new_count

        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)


    result = []
    for element in counts:
        if counts[element] == k:
            result.append(element)

    return result


print(findK(TreeNode(2, TreeNode(2), TreeNode(3, None, TreeNode(4))), 2) , 2)
print(findK(TreeNode(2, TreeNode(2, TreeNode(24), None), TreeNode(3, None, TreeNode(4))), 1), [24, 3, 4])

print(findK(TreeNode(None), None))

