# find Max Element in a Linked List (recursive)"

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findMax(node, max=0):
  if node is None:
    return max
  if node.value > max:
    max = node.value
  return findMax(node.next)
