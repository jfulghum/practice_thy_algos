
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

# Prompt
# Given a linked list and a target k, return a linked list containing every kth element in the list.
# Function Signature
# function everyKthNode(node, target)
# Expected Runtime
# O(n)
# Examples
# 1 -> 3 -> 6 -> 2 -> 8 -> 9, 3 => 6 -> 9
      
def everyKthNode(node, k):
  sentinel = ListNode(0)
  sentinel.next = node
  curr = sentinel.next
  count = 0
  sentinel2 = sentinel
  new = sentinel2
  while curr: 
    count +=1 
    if count % k == 0:
      new.next = curr
      new = new.next
    curr = curr.next
  return sentinel2.next 

LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(8))))
# print(everyKthNode(None, 2)) # empty
result = everyKthNode(LL1, 2) # 4, 8


def arrarify(node):
  while node:
    print(node.value)
    node = node.next

arrarify(result)
