
# Given an integer k, create a linked list representing the first k values of the Fibonacci sequence.
# For example, given k = 1, return this list: 1
# Given k = 6, return this list: 1 -> 1 -> 2 -> 3 -> 5 -> 8


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def solution(k):
    if k == 0:
        return []
    if k == 1:
        return ListNode(1)
 
    previous = ListNode(0)
    current = ListNode(1)
    result = current
    
    for _ in range(k - 1):
        new = ListNode(previous.value + current.value)
        current.next = new
        previous = current
        current = new
    return result
