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
