# -- JOHANNA --

def reduce(head, accumulator_func, initialVal):
  curr = head
  accumulator = initialVal
  while curr:
    accumulator = accumulator_func(accumulator, curr)
    curr = curr.next
  return accumulator

reduce([1, 5, 10], function(acc, curr) {
  return acc + curr
}, 0)



def map(head, mapper_func):
  if head is None:
    return None
  new_node = ListNode(0)
  new_curr = new_node
  curr = head
  while curr:
    new_curr.next = mapper_func(curr)  # this needs to be new_curr.next! you need to create these nodes attached to each other. 
    new_curr = new_curr.next
    curr = curr.next
  return new_node.next
    
  
 def filter(head, testFunction) :
    new_node = ListNode(0)
    new_curr = new_node
    curr = head
    while curr:
      if testFunction(curr):
        new_curr.next = ListNode(curr.value)  # you have to create the new node here! or else you'll be like a tree all these things will be pointing to curr
        new_curr = new_curr.next
      curr = curr.next
    return new_node.next

