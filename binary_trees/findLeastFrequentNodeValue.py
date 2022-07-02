# Given a binary tree with node values represented as integers, find and return the least occurring  tree node value

   #     2
    #    / \ 
    #   2   2

    # stack traverse 
    # hash count the values 
    # return the key with the lowest value count 

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def findLeastFrequentNodeValue(root):
    if root is None:
        return root
    values_count = {}
    stack = [root]
    while stack:
        node = stack.pop()
        if values_count.get(node.value):
            values_count[node.value] += 1
        else:
            values_count[node.value] = 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    lowest = float('inf')            
    for key, value in values_count.items():
        if value < lowest:
            lowest = key
    return lowest


tree1 = TreeNode(2, TreeNode(2), TreeNode(2))
tree2 = TreeNode(2, TreeNode(2), TreeNode(3))
tree3 = TreeNode(4)
    
print(findLeastFrequentNodeValue(tree1) == 2 )
print(findLeastFrequentNodeValue(tree2) == 3 )
print(findLeastFrequentNodeValue(tree3)  == 4 )
