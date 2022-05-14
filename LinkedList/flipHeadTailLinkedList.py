# In order to make the tail the new head, you want to make last point to the node after head. second_to_last point to head, and head point to None. That will cause the flip.

# But you'll have to handle the case of a length-2 list separately.

# Also head = last doesn't change the head pointer in reality. Just return tail once you've changed the links as described.
# last = head.next
# second_to_last = head 
# head = None

# class ListNode:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = None

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

def flipHeadTailLinkedList(head):
  if head is None or head.next is None:
      return head
  first = head    
  last = head.next 
  second_to_last = head.next # initialize to head.next in case length of 2
  
  while last.next:
      second_to_last = last
      last = last.next
     
  last.next = first.next
  second_to_last.next = first
  
  head = last
  second_to_last.next.next = None 

  return last

LL1 = ListNode(1, ListNode(3, ListNode(4, ListNode(5))))
LL2 = ListNode(1, ListNode(3))

print(arrayify(LL1))
print(arrayify(flipHeadTailLinkedList(LL1)))

print(arrayify(LL2))
print(arrayify(flipHeadTailLinkedList(LL2)))
