""" /*
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

               p1 n1  p2. n2
Input: head = [1, 2,  3,  4,  5], k = 2
                      
             n2next = n2->next. = 5
             p1->next = n2
             n2->next = n1->next

             p2->next = n1
             n1->next = n2next
[1, 4, 3, 2, 5]
            
Run time = k + (n-k) = n
Place = O(1)
               
Output: [1,4,3,2,5]

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Input: head = [1,2,3,4,5], k = 4
Output: [1,4,3,2,5]


*/ """
from typing import List


class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next
    def stringify(self):
        curr = self
        LLString = "["

        while curr.next:
            LLString += str(curr.value) + "-> "
            curr = curr.next
        LLString += str(curr.value) + "]"

        return LLString
    def __repr__(self):
        if self.next is None:
            return f"{self.value} "
        else:
            return f"{self.value} -> {self.next}"
"""

"""
def swapNth(head: ListNode, target: int):
    if not head:
        return head
    #curr = head
    
    
    newhead =  ListNode(-1, head)

    slow = newhead
    fast = newhead
    p1 = None

    for i in range (0,target): #move the fast ptr
        p1 = fast
        fast = fast.next

    temp = fast
    p2 = None
    #fast = nth from the beginning
    while fast.next:
        p2 = slow
        slow = slow.next
        fast = fast.next
    #slow = nth from the endd
    p2 = slow
    slow = slow.next
    """
        n2next = n2->next. = 5
             p1->next = n2
             n2->next = n1->next

             p2->next = n1
             n1->next = n2next

             1 2 3 4 5

             5 2 3 4 1 
    """
    n1 = temp
    n2 = slow
        
    n2next = n2.next

    p1.next = n2
    n2.next = n1.next
        
    p2.next = n1
    n1.next = n2next

    
    #temp.value, slow.value = slow.value, temp.value
    
    return newhead.next


'''
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Input: head = [1,2,3,4,5], k = 4
Output: [1,4,3,2,5]

'''
a = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

b = ListNode(7,ListNode(9,ListNode(6,ListNode(6,ListNode(7,ListNode(8,ListNode(3,ListNode(0,ListNode(9,ListNode(5))))))))))
c = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

print(swapNth(a,1))
print(swapNth(b,5))
print(swapNth(c,4))
    
