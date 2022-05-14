def solution(head):
    tail = head
    if head is None or head.next is None:
        return head
        
    first = head
    last = head
    
    while last.next:
        last = last.next
    
    head = first.next
    first.next = None
    last.next = first
    
    
    return head
