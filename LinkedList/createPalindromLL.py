class ListNode:
  def __init__(self, value = 0, next = None): 
    self.value = value
    self.next = next

      
# Given a linked list and a target value, return the index of the first occurrence of that value in the linked list. The index should be zero-indexed.
# Function Signature

# Examples
# [1, 4, 5] => 1 -> 4 -> 5 -> 4 -> 1

def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array
      
def createPalindromLL(input):
  # make an array of the elements
  curr = input
  elements = []
  while curr:
    elements.append(curr.value)
    prev = curr
    curr = curr.next 
  elements.pop()
  while elements:
    print(elements)
    prev.next = ListNode(elements.pop())
    prev = prev.next

  return input 

LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(arrayify(createPalindromLL(LL1)))
  
