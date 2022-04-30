# Insert Target Element in Sorted Linked List (iterative)

class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

def insert(head: ListNode, target: int) -> ListNode:
    curr = head
    if curr is None:
        newNode = ListNode(target)
        return newNode

    if target < curr.value:
        newNode = ListNode(target)
        newNode.next = curr
        return newNode

    while curr.next and curr.next.value < target:
        curr = curr.next
    newNode = ListNode(target)
    newNode.next = curr.next
    curr.next = newNode

    return head


# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(4)))
LL2 = ListNode(-3, ListNode(-2, ListNode(-1)))
print(arrayify(insert(LL1, 2))) # [1, 2, 3, 4]
print(arrayify(insert(LL2, -4))) # [-4, -3, -2, -1]
print(arrayify(insert(LL2, 0))) # [-3, -2, -1, 0]
print(arrayify(insert(None, 1))) # [1]
