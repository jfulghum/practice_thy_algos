def get_cheapest_cost(rootNode):
  if len(rootNode.children) == 0: return rootNode.cost
  total = float('inf')
  for childNode in rootNode.children:
    temp = get_cheapest_cost(childNode)
    if temp < total:   #Because of this, it's always finding cheapest cost for all the children
      total = temp
  return rootNode.cost + total

class Node:
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

n1 = Node(20)
n2 = Node(20)
n3 = Node(10)
n4 = Node(25)
n5 = Node(66)
n1.children.append(n2)
n1.children.append(n4)
n2.children.append(n3)

print(get_cheapest_cost(n5))
