class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	first = head
    second = head
	counter = 1
	while counter <= k:
		second = second.next
		counter +=1
	if second is None:
		#remove head
		head.value = head.next.value
		head.next = head.next.next
		return
	while second.next is not None:
		#move first up
		first = first.next 
		second = second.next
	#remove node where first is now
	first.next = first.next.next
