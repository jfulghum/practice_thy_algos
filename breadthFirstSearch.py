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

// Oliver is missing his favorite hat and is asking his friends at the dog park if they've seen it. Each dog either has seen it or suggests a list of other dogs to ask. Return the name of the dog who has seen the hat.

/**
 * Approaches:
 * queue = []
 * Look up bestfriend (Loki -> list)
 * push the keys into the queue 
 * while the queue is filled
 *  dogFromQueue = queue.pop()
 *  check if the "HAT" exists from the dogFromQueue
 *  else the dogFromQueue
 *    check the dog has other members and push them into the queue
 * 
 * return null
 */

function findHat(dogs, bestFriend){
  let queue = [...dogs[bestFriend]]; 
  let dogsAsked = new Set()
  while(queue.length) {
    let dogFromQueue = queue.pop();
    if (!dogsAsked.has(dogFromQueue)) {
      if(dogs[dogFromQueue][0] == "HAT") {
        return dogFromQueue;
      } else {
        dogsAsked.add(dogFromQueue)
        // push the additonal dogs into the queue
        dogs[dogFromQueue].map(dog =>  {
          if (!dogsAsked.has(dog)) {
            queue.push(dog)
          } 
        });            
      }
    } 
  }
  return null;
}

// Target runtime and space complexity:
//  O(n)
// Examples:
const dogs = {
  'Carter': ['Fido', 'Ivy'],
  'Ivy': ["HAT"], // Ivy has seen the hat
  'Loki': ['Snoopy'],
  'Pepper': ['Snoopy', 'Ivy'], 
  'Snoopy': ['Pepper'],
  'Fido': []
};
console.log(findHat(dogs, 'Loki')); // returns 'Ivy'
console.log(findHat(dogs, 'Fido')) // null
console.log(findHat(dogs, 'Pepper')); // returns 'Ivy'

