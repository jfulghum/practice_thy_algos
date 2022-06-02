'''

Given a binary search tree where all nodes have integer values, return the floor and ceil of a target number.
The floor is the largest element that is smaller than or equal to the target, 
The ceil is the smallest element that is greater than or equal to the number

Examples

For example:
.     3
.  1    5
    2

    [5, null]
    null
target: 4 returns [3, 5]
target: 2 returns [1, 3]

if no ceiling or no floor:
  return null

target = 3
null


left 
right
mid

[]

Base case:
- if node is None:
    return None
if node.value == target:
    return [target, target]

if target < node.value:
  arr[1] = Math.min(arr[1], node.val)
  binarySearch(node.left, arr)
else:
  arr[0] = Math.max(arr[0], node.val)
  binarySearch(node.right, arr)

return arr[0] and arr[1] ? arr : None



'''

while(cur){
    if cur.value == target:
    return [target, target]

    if target < cur.value:
        arr[1] = Math.min(arr[1], node.val)
        cur = cur.left
    else:
        arr[0] = Math.max(arr[0], node.val)
        cur = cur.right
    }

# the below way is higher space complexity, the above way has better space complexity. 

import math

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def floor_ceil(node, target):
    return helper(node, [None, None], target)


def helper(node, output, target):
    if not node:
        return output
    if node.value == target:
        return [target, target]

    if target < node.value:
        output[1] = min(output[1] or math.inf, node.value)
        helper(node.left, output, target)
    else:
        output[0] = max(output[0] or -math.inf, node.value)
        helper(node.right, output, target)

    return output

'''
     8
    /
   3 
  / \
 1   6
    /
   4 

target: 5
'''

tree = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4))))
print(floor_ceil(tree, 5), '[4, 6]')

'''
.     3
.  1    5
    2
'''
tree1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(5, None, None))


'''


    5
  5
4

'''
# tree3 = TreeNode(5, TreeNode(5, TreeNode(4)))
# print(floor_ceil(tree3, 3),[None, 4])

print(floor_ceil(tree1, 3), [3, 3])
print(floor_ceil(tree1, 4), [3, 5])
print(floor_ceil(tree1, 6), [5, None])
print(floor_ceil(tree1, -5), [None, 1])
print(floor_ceil(None, 2), [None, None])
