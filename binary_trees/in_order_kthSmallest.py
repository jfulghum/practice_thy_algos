class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

def kthSmallest(root, k) -> bool:
  def storeNodes(root: Node) -> None:
    if not root:
      return

    storeNodes(root.left)
    sortedList.append(root.val)
    storeNodes(root.right)

  sortedList = []
  if root:
    storeNodes(root)
  
  return sortedList[k-1]


oneNode = Node(1)
print(kthSmallest(oneNode, 1) == 1)

#           30
#     20          40
#  10   25      33   60
complete3levels = Node(30,
  Node(20,
    Node(10),
    Node(25)),
  Node(40,
    Node(33),
    Node(60)))

print(kthSmallest(complete3levels, 1) == 10)
print(kthSmallest(complete3levels, 2) == 20)
print(kthSmallest(complete3levels, 4) == 30)
print(kthSmallest(complete3levels, 7) == 60)

#           30
#     20         40
#  10   25     33   60
#   15 23    32       80
partial4levels = Node(30,
  Node(20,
    Node(10,
      None,
      Node(15)),
    Node(25,
      Node(23),
      None)),
  Node(40,
    Node(33,
      Node(32),
      None),
    Node(60,
      None,
      Node(80))))

print(kthSmallest(partial4levels, 1) == 10)
print(kthSmallest(partial4levels, 2) == 15)
print(kthSmallest(partial4levels, 4) == 23)
print(kthSmallest(partial4levels, 6) == 30)
print(kthSmallest(partial4levels, 8) == 33)
print(kthSmallest(partial4levels, 11) == 80)
