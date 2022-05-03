

class ListNode:
  def __init__(self, value = 0, next = None): 
    self.value = value
    self.next = next  

def numPairs(curr):
  numPairs = {}
  count_pairs = 0
  
  while curr:
    numPairs[curr.value] = numPairs.get(curr.value, 0) + 1
    if numPairs.get(curr.value) == 2:
      count_pairs += 1 
      numPairs[curr.value] = 0
    curr = curr.next
  return count_pairs





# Expected Runtime
# O(n)
# Examples
# 1 -> 2 -> 2 -> 3 -> 3 -> 3 returns 1 (only the element 2 appeared twice)
# Expected Questions
# If you were presented this question in an interview, these are some questions(s) you might want to ask:
# Q: Can the list be empty?
# A: Yes.
  
LL1 = ListNode(1, ListNode(4, ListNode(4)))
print(numPairs(LL1)) # 1
LL2 = ListNode(1, ListNode(4))
print(numPairs(LL2)) # 0

LL3 = ListNode(4, ListNode(4)) # 1
print(numPairs(LL3)) 
