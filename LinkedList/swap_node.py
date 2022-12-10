"""
# Engineering Method:
# 1. Step Through the Problem
# -come up with "happy case" examples
# -come up with edge cases /logical edge cases
# 2. Identify and explore possible solutions
# - identify simple solution 
# - work out some example cases manually
# - work out expected time and space complexity
# - proactively point out pros and cons to own solution
# 3. Choosing a solution
# - eye on time, give yourself at least half of the time to code
# - be confident in an approach
# - consider time and space 
# - CONSIDER DIFFICULTY OF IMPLEMENTATION/ time constraint to code
# 4. Build it
# - Initiate the transition to code by asking if interviewer needs anything to be clarified before starting
# - The interviewer might suggest to code
# 5. Test it
# - you may discover implementation level edge cases
# - test minimum and smallest test cases to illustrate different cases
# - when you discover a bug DO NOT TRY THINGS RANDOMLY
# - it's better to NOT solve bugs with special cases
#     = think about what category of cases you're missing and fix the ENTIRE category of bugs


Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.) [See examples below]
This problem is a sub-case of the common interview question 'swap nodes in groups of k', where k = 2. If fellows are able to solve this quickly, consider asking for k > 2 as a follow-up.

Input: 1->2->3->4
Output: 2->1->4->3

Input: null
Output: null

Input: 1
Output: 1

Input: 1->2->3
Output: 1->3->2 

Input: 1->2->3->4->5
Output: 1->3->2->5->4

Target runtime and space complexity:
O(N) time, O(1) space


Input: 1->2->3->4
2->1->4->3
node = 1->2->3->4
reattach = 2
node.next = 2



# loop thru the LL and find count

Even Case 
sentinel = node.next

while node.next:
    nodeNode = node.next
    reattach = nodeNode.next 
    node.next = reattach
    nodeNode.next = node

    node = reattach

Odd Case 
sentinel = node
node = node.next (skips first node)
while node.next:
    nodeNode = node.next
    reattach = nodeNode.next 
    node.next = reattach
    nodeNode.next = node

    node = reattach

return sentinel

def swapPairs(self, node: ListNode) -> ListNode:


"""
class ListNode():

  def __init__(self, x, next = None):

    self.value = x

    self.next = next


def swapPairs(node):
    if node is None:
        return None 
        
    count = 0 
    curr = node
    sentinel = None
    while curr:
        count += 1
        curr = curr.next 

    prev = None

    if count % 2 == 0:
        sentinel = node.next

        while node and node.next:
            
            nextNode = node.next
            reattach = nextNode.next 
            
            node.next = reattach
            nextNode.next = node

            if prev:
                prev.next = nextNode

            prev = node

            node = reattach

    else: 
        sentinel = node
        node = node.next 
        future = None
        if node.next:
            future = node.next # 3
            print(future.value, "\n")
        
        while node and node.next:
            
            nextNode = node.next
            
            reattach = nextNode.next 
            
            node.next = reattach
            nextNode.next = node

            if future:
                
                sentinel.next = future #3 
                future = None

            if prev:
                prev.next = nextNode

            prev = node 

            node = reattach

    
    return sentinel



tEven = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,ListNode(7, ListNode(8))))))))
tNull = None
tOdd = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,ListNode(7)))))))

def printLL(node):
    #print(node)
    while node != None:
        print(node.value)
        node = node.next
        

#printLL(swapPairs(tEven))
# printLL(swapPairs(tNull))
printLL(swapPairs(tOdd))
