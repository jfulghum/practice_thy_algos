# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		queue = [self]
		while len(queue) > 0:
			current = queue.pop(0)
			for child in current.children:
				queue.append(child)
			array.append(current.name)
		return array

	
# Target runtime and space complexity:
#  O(n)
# Examples:


def findHat(dogs, bestFriend):
    dogsToAsk = [bestFriend]
    dogsAlreadyAsked = set()
    while(len(dogsToAsk) > 0):
        nextDogToAsk = dogsToAsk.pop();
        if nextDogToAsk in dogsAlreadyAsked:
            continue
        if (dogs[nextDogToAsk][0] == 'HAT'):
            return nextDogToAsk
        dogsAlreadyAsked.add(nextDogToAsk)

        newDogsToAsk = dogs[nextDogToAsk]
        dogsToAsk.extend(newDogsToAsk)
    return -1



dogs = {
  'Carter': ['Fido', 'Ivy'],
  'Ivy': ["HAT"], # Ivy has seen the hat
  'Loki': ['Snoopy'],
  'Pepper': ['Carter'],
  'Snoopy': ['Pepper'],
  'Fido': []
}

print(findHat(dogs, 'Loki')) # returns 'Ivy'

