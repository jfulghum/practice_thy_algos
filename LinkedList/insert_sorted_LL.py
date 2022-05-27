
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

  
def insert(head: ListNode, value: int) -> ListNode:
  newNode = ListNode(value)
  if head is None:
    return newNode
    
  if head.value > value:
    newNode.next = head
    return newNode

  if head.next is None:
    head.next = newNode
  else:
    head.next = insert(head.next, value)

  return head


# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(4)))
LL2 = ListNode(-3, ListNode(-2, ListNode(-1)))
print(arrayify(insert(LL1, 2))) # [1, 2, 3, 4]
print(arrayify(insert(LL2, -4))) # [-4, -3, -2, -1]
print(arrayify(insert(LL2, 0))) # [-3, -2, -1, 0]
print(arrayify(insert(None, 1))) # [1]
