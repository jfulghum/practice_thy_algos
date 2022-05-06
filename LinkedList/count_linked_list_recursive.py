class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
    
def count(node: ListNode) -> int:
  if node is None:
    return 0
  else:
    return count(node.next) + 1
  

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None)) # 0
print(count(LL1)) # 3
print(count(ListNode())) # 1
