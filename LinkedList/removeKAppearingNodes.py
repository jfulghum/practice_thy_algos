# Given the head node of a singly linked list, find nodes where they have already appeared (k) or more times.
# Return the head node of the new linked list, after deleting/removing the nodes.
# If a node appears more than once in a list, only the nodes that are kth or higher must be deleted. You can still retain the nodes leading up to the kth occurrence.
# Function Signature: 
'''
1->2->3->4->1 k=2
1->2->3->4->
1->2->3->1->1 k=2 return 1->2->3->


Edge cases:
    1->2->3->1->1 k=2 return 1->2->3->
    1->2->3->1 k=0 return 1->2->3->1
    1->2->3->2->1->4 k=2 return 1->2->3->4
    None k=1 return None
    1-> k=1 return 1->

Solutions:
    -create sentinel node that tracks head
    -count as we go through list and once count > k check if value equals k. (keeps track of LL location)
    -keeps track of frequency of node value(hashTable/dictionary)
    -if so, previous next points to current next
    - return head
'''

def removeKAppearingNodes(head, k):
    if not head:
        return head
    if k == 0:
        return head

    value_to_freq = dict()
    ll_index = 0
    sentinel = head
    previous = head
    #1->1->2 k=2
    #1->2
    while sentinel:
        ll_index += 1
        value_to_freq[sentinel.value] = value_to_freq.get(sentinel.value, 0) + 1
        if value_to_freq[sentinel.value] >= k and ll_index >= k:
            previous.next = sentinel.next
        else:
            previous = sentinel
        sentinel = sentinel.next
        
        
    return head


class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next


def arrayify(head):

    array = []

    ptr = head

    while ptr != None:

        array.append(ptr.value)

        ptr = ptr.next

    return array

t1 = ListNode(4,ListNode(3,ListNode(4,ListNode(1,ListNode(5)))))
print(arrayify(removeKAppearingNodes(t1,2)))#[4,3,1,5]

# list = [4, 3, 4, 1, 5], k = 2 => [4, 3, 1, 5]
# list = [1, 1, 2] => k = 2 => [1, 2]
# list = [1, 2, 3] => k = 3 => [1, 2, 3]

t2 =  ListNode(1, ListNode(1, ListNode(2)))
print(arrayify(removeKAppearingNodes(t2, 2)))#[1,2]

t3 = ListNode(1, ListNode(2, ListNode(3)))
print(arrayify(removeKAppearingNodes(t3, 3)))#[1,2,3]

t4 = ListNode(1, ListNode(2, ListNode(3)))
print(arrayify(removeKAppearingNodes(t3, 1))) #[1] 


# 4 -> 3 -> 4 -> 1 -> 5, k = 2 should return 4 -> 3 -> 1 -> 5
# 1 -> 1 -> 2, k = 2 should return 1 -> 2
# 1 -> 2 -> 3, k = 3 should return 1 -> 2 -> 3
