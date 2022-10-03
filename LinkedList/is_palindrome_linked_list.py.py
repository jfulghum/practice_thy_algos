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
    

# another way:

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseLL(head):
    prevNode, currNode = None, head
    while currNode:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode, currNode = currNode, nextNode
    return prevNode
    
def compare(list1, list2):
    while list1 and list2:
        if list1.value == list2.value:
            list1 = list1.next
            list2 = list2.next
        else:
            return False
    return True

def solution(head):
    reverse = reverseLL(head)
    
    return compare(head, reverse)
    
#  1 -> 2 -> 3
#  3 -> 2 -> 1   

        
