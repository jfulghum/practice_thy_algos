#insert in order 

def solution(list, target):
    if list is None:
        return ListNode(target)
    
    curr = list
    if curr.value > target:
        head = ListNode(target)
        head.next = curr 
        return head
    
    while curr.next:
        prev = curr
        curr = curr.next
        if curr and curr.value > target:
            prev.next = ListNode(target)
            prev.next.next = curr
            return list
        
    curr.next = ListNode(target)
    return list



# insert before target

def solution(head, target, value):
    curr = head
    if curr.value == target:
        node = ListNode(value)
        node.next = curr 
        return node
    
    while curr.next:
        prev = curr
        curr = curr.next
        if curr and curr.value == target:
            prev.next = ListNode(value)
            prev.next.next = curr
            return head
            
    return head
            
        
            

