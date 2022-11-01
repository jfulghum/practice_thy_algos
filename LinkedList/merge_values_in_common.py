# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def solution(a, b):
    if a is None:
        return None
    if b is None:
        return None 
    
    sentinel = ListNode(float("-inf"))
    curr = sentinel
    
    while a and b:
        if a.value == b.value:
            curr.next = a
            a = a.next
            b = b.next
            curr = curr.next
        elif a.value < b.value:
            a = a.next
        else:
            b = b.next
            
            
    return sentinel.next
            
        
        

