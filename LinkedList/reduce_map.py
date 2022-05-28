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
    new_curr.next = mapper_func(curr)
    new_curr = new_curr.next
    curr = curr.next
  return new_node.next
    
