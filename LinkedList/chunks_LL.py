
# // if k is less than 1, return null
# // if k is one, return an array of the values
# // if list is empty, return k empty arrays

# // determine length of list
# // minNodes -> floor of list length / k -> general # of nodes for each array
# // modulo of list % k -> leftover nodes

# // declare empty result array
# // curr pointer starting at list head

# // k loops
#   // if curr is ever null, break out of iteration but still push new array 
#   // iterate forward by minNodes nodes -> push value to a new array
#   // if there are leftovers, iterate one more and decrement leftover count
#   // push new array to result array

# // return result array

# Find length of array
# find left overs

class LinkedList():
  def __init__(self, value, next=None):
    self.value = value 
    self.next = next


def chunk_segments(curr, k):

  if k == 0:
    return None
  

  def get_length(curr):
    n = 0
    while curr:
      n += 1 
      curr = curr.next

    return n

  length = get_length(curr)
  minNodes = length // k
  leftoverNodes = length % k 

  result = []

  for i in range(k):
    chunk = []
    
    for j in range(minNodes):
      if curr:
        chunk.append(curr.value)
        curr = curr.next

    if leftoverNodes:
      leftoverNodes -= 1
      chunk.append(curr.value)
      curr = curr.next

    result.append(chunk)

  return result
      
      
    
list1 =  LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
print(chunk_segments(list1, 5))


list2 = LinkedList(1, LinkedList(2, LinkedList(3)))
print(chunk_segments(list1, 5), [[1], [2], [3], [4], [5]]);
print(chunk_segments(list2, 5), [[1], [2], [3], [], []])
print(chunk_segments(list1, 0), None);
print(chunk_segments(None, 1), [[]]);
print(chunk_segments(list1, 2), [[1, 2, 3], [4, 5]])
  
      
    
