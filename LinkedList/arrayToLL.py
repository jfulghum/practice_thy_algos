class LLNode:
  def __init__(self, val, next = None):
    self.value = val
    self.next = next

def arrayToLL(array):
  if not array:
    return None
  sentinel = LLNode(0)
  sentinel.next = LLNode(array[0])
  curr = sentinel.next
  for i in range(len(array) - 1):
    curr.next = LLNode(array[i + 1])
    curr = curr.next
  return sentinel.next


def printList(head):
    if not head:
        return "<empty>"

    parts = [];
    while head:
       parts.append(str(head.value));
       head = head.next;

    return " -> ".join(parts);
# Expected Runtime
# O(n)
# Examples
# [1, 2] => 1 -> 2
# [] => null
# [1] => 1
LL =  arrayToLL([1, 2, 3, 4, 5])

print(printList(LL))
# => 1 -> 2 -> 3 -> 4 -> 5
# Expected Questions
# If you were presented this question in an interview, these are some questions(s) you might want to ask:
# Q: Can the array be empty?
# A: Yes.
