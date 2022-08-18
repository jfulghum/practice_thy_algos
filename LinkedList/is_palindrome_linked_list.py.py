# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):
    slow = head
    stack = []
      
    ispalin = True
  
    while slow != None:
        stack.append(slow.value)
        slow = slow.next
  
    while head != None:
        i = stack.pop()
          
        if head.value == i:
            ispalin = True
        else:
            ispalin = False
            break
        head = head.next
          
    return ispalin
    

