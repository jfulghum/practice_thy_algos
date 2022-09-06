CHALLENGE

Given a linked list with each node representing a digit in an integer, add 1 to the number. The number has the most significant digit as the head and the least significant digit as the tail.

What if it's too big to be stored in an integer or long?
How can it be done in place without using another collection?

9->-9->9
1->0->0->0

1 -> 9

reverse: 9 -> 1
turns 9 to 0, .next +1
'''

#reverses by changing the links between nodes
def reverse(head):
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev

def addOneLL(head):
    if head is None:
        return None
    reverse(head)

    if head.val == 9:
        new_head = 0
    else:

    
    addOneLL(head.next)
        
    return reverse(new_head)
