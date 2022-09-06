'''
===================
PROBLEM STATEMENT
===================
Write a program to recursively alternate printing nodes.  You are not allowed to use loop constructs. You can assume that the head node should always be printed first and then give the option to skip the head as a follow-up. Here is some starting code to implement a linked list in Python.


EXAMPLE:
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

printAlternate(n1)  # should print 1 -> 3 -> 

m1 = Node(1)
m2 = Node(2)
m3 = Node(3)
m4 = Node(4)
m5 = Node(5)
m6 = Node(6)
m7 = Node(7)
m8 = Node(8)

m1.next = m2
m2.next = m3
m3.next = m4
m4.next = m5
m5.next = m6
m6.next = m7

printAlternate(m1) # should print 1 -> 3 -> 5 -> 7 ->

'''
    #check the base condition
    #if not head:
        #return
    #console.log(head.val)
    #if head.next
        #head=head.next
        #printAlternate(head.next)
    #else:
        #return 

class Node:
  def __init__(self, val=None):
    self.val = val
    self.next = None

def printLL(head: Node) -> None:
  i = 0 # only print the first 20

  while head and i < 20:
    print(str(head.val) + " -> ", end="")
    head = head.next
    i += 1

def printAlternate(head):
    if not head:
        print("\n")
        return 
    
    print(str(head.val) + " -> ", end="")
    if head.next: 
        head = head.next
        printAlternate(head.next)
    else:
        print("\n")
        return


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

printAlternate(n1) # 1 -> 3  ->


n4 = Node(1)
printAlternate(n4) # 1 ->


n5 = Node(1)
n6 = Node(1)
n5.next = n6
printAlternate(n5) # 1 ->


printAlternate(None) # nothing

