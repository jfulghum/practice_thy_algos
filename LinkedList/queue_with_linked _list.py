# Queue Class with Linked List

# Your class will need a head and tail pointer, as well as a field to track the current size.
# Enqueue adds a new value at one side.
# Dequeue removes and returns the value at the opposite side.

# A doubly linked list is one of the simplest ways to implement a queue. You'll need both a head and tail pointer to keep track of where to add and where to remove data. Using a doubly linked list means you can do both operations without walking the whole list and all modifications of the list are at the ends.


class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
      
class LLQueue:
  def __init__(self):
        self.front = self.rear = None

  def isEmpty(self):
        return self.front == None
    
  def enqueue(self, item):
    temp = ListNode(item)
    if self.rear == None:
      self.front = self.rear = temp
      return
    self.rear.next = temp
    self.rear = temp
    
  def dequeue(self, item = None):
    if self.isEmpty():
      return
    temp = self.front
    self.front = temp.next

    if(self.front == None):
        self.rear = None
      
    return temp.value
    
  def size(self):
    count = 0 
    curr = self.front
    while curr:
      count += 1
      curr = curr.next
    return count

    
# Expected Runtime
# O(1) for all methods!
# Examples
q = LLQueue()
print(q.size()) # 0

q.enqueue(2)
q.enqueue(3)
print(q.size()) # 2
print(q.dequeue()) # 2
print(q.size()) # 1
print(q.dequeue()) # 3
