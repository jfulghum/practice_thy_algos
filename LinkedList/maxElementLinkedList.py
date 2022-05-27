# find Max Element in a Linked List (recursive)"

class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
# def findMax(node: ListNode, max=0) -> int:
#     if node is None:
#       return max
#     if node.value > max:
#       max = node.value
#     return findMax(node.next, max)
        
def findMax(node: ListNode) -> int:
    if node.next is None:
      return node.value

    return max(node.value, findMax(node.next))

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
print(findMax(LL1)) # 5
print(findMax(LL2)) # 7
print(findMax(LL3)) # 0
print(findMax(ListNode(1))) # 1
