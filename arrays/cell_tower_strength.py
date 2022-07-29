"""
You are given an array representing the positions of cell towers along a 1 dimensional line. You are given a second array representing positions of customers across the same 2 dimensional line. Given these two inputs, you must determine a signal strength k such that every customer is covered by at least one cell tower. All cell towers must have the exact same signal strength and covers customers to its left and right equally.

These arrays can be imagined as street addresses along a road. At each address there might be a customer and there might also be a tower at that location.

Function Signature: 
    def search(listener, towers):

Target runtime and space complexity:
    Runtime: O(n)
    Space: O(1)

Examples:

Let's say cell towers are at: [0, 2, 6, 10]
and customers are at: [0, 5, 11]
In this case, you only need a cell distance of 1, because customer 5 would be covered by 6 and customer 11 would be covered by 10.
If the customers were at: [0, 4, 13], you'd need a distance of 3 in order for customer 13 to be covered by 10.


examples:
towers = [4, 6]
customer = [2]
answer => 2

towers = [4, 6]
customer = [1]
answer => 3

towers = [4, 6]
customer = [9]
answer => 3

towers = [4, 6, 8]
customer = [5, 6]
answer => 1

max = 1

t: [0, 2, 6, 10]
             i

c: [0, 5, 11]
          i

max = 1
currentDistance

t: [4, 6, 8]
    i

c: [5, 6]
    i

return None if no c or t

# init a max = - infinity
# O(n) pointers, start at index 0 for both,
# currentDistance = abs(customer, tower)
    # check to see if moving to the next tower decreases the currentDistance? 
        move tower pointer
        update currentDistance   
    # else
        # update max
        # move customer pointer
  return max
"""

def search(listener, towers):
    if not listener or not towers:
        return None
    maxSoFar = float('-inf')
    towerIdx = 0
    lisIdx = 0
    while lisIdx < len(listener):
        currentDistance = abs(listener[lisIdx] - towers[towerIdx])
        while towerIdx < (len(towers) - 1) and abs(listener[lisIdx] - towers[towerIdx + 1]) < currentDistance:
            towerIdx += 1
            currentDistance = abs(listener[lisIdx] - towers[towerIdx])
        maxSoFar = max(maxSoFar, currentDistance)
        lisIdx += 1
    return maxSoFar


def check(i, output, expected):
    if expected == output:  
        print(f"[{i}] Test case passed with output of {output}")
    else:
        print(f"[{i}] Test case failed. Expected {expected}, received {output}.")

check(1, search([1,2,3], [1,2,3]), 0)
check(2, search([0, 5, 11], [0, 2, 6, 10]), 1)
check(3, search([3, 8], [5]), 3)
check(4, search([1, 6], [5, 6]), 4)
check(5, search([], []), None)

