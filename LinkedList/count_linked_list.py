
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

      
def count(node: ListNode) -> int:
    if node is None:
        return 0
    return 1 + count(node.next)

LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None)) # 0
print(count(LL1)) # 3
print(count(ListNode())) # 1

def count_iterative(node: ListNode) -> int:
  curr = node
  sum = 0
  while curr:
    sum += 1
    curr = curr.next
  return sum

print(count_iterative(None)) # 0
print(count_iterative(LL1)) # 3
print(count_iterative(ListNode())) # 1
