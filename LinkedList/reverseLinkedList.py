# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    previousNode, currentNode = None, head
	while currentNode is not None:
		nextNode = currentNode.next
		#turn the direction around
		currentNode.next = previousNode
		#move the pointers up
		previousNode = currentNode
		currentNode = nextNode
	return previousNode
