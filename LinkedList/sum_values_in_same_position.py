# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(list1, list2):
    if list1 is None:
        return None 
        
    sentinel = ListNode(0)
    curr = sentinel
        
    while list1:
        curr.next = ListNode(list1.value + list2.value)
        curr = curr.next
        list1 = list1.next
        list2 = list2.next
        
    return sentinel.next
