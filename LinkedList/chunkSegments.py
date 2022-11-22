# Given the head node of a linked list and any number (k), break your list into (k) consecutive chunks, with no two chunks should have a size differing more than one.
# The result chunks should be in the same original order, and chunks occurring earlier should never be smaller than later chunks.
# Return an array of all (k) chunks.
# Function Signature: 
# function chunkSegments(head, n)
# Target runtime and space complexity:
# O(n)

# Approach, go through the ll once, find the length of the LL so you can determine the length of the chunks. 


# count_node = head
# total_length = 0
# while count_node:
#  total_length += 1
#  count_node = count_node.next

# sub_length = total_length // k
# remainder  = total_length % k
# result = []
# chunk = []
# curr = head
# while curr:
#   chunk.append(curr.value)
#   curr = curr.next
    # if len(chunk) === sub_length:
        # if remainder:
            # chunk.append(curr.value)
            # curr = curr.next
            # remainder -= 1
        # result.append(chunk)
        # chunk = []

# while len(result) < k:
    # result.append([])

# return result
import math 

class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

"""
# 1 -> 2 -> 3, k = 5 should return [[1], [2], [3], [], []]
k = 5 
n = 3
s = 3 // 5 = 0
r = 
"""
def chunkSegments(head, k):
    count_node = head
    total_length = 0
    while count_node:
        total_length += 1
        count_node = count_node.next

    sub_length = total_length // k
    remainder = total_length % k

    if sub_length == 0 and head:
        sub_length = 1
        remainder = 0

    result = []
    chunk = []
    curr = head
    while curr:
        chunk.append(curr.value)
        curr = curr.next
        if len(chunk) == sub_length:
            if remainder:
                chunk.append(curr.value)
                curr = curr.next
                remainder -= 1
            result.append(chunk)
            chunk = []

    while len(result) < k:
        result.append([])

    return result




# Examples:
# Example 1

# 1 -> 2 -> 3 -> 4 -> 5, k = 5 should return [[1], [2], [3], [4], [5]]
ll1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(chunkSegments(ll1, 5))

# Example 2
# 1 -> 2 -> 3, k = 5 should return [[1], [2], [3], [], []]
# Example 3
ll2 = ListNode(1, ListNode(2, ListNode(3)))
print(chunkSegments(ll2, 5))

ll3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print(chunkSegments(ll3, 2))
# 2 -> 2 -> 3 -> 4 -> 5 -> 6 -> 4 -> 8 -> 9 -> 10 -> 11, k = 3 should return [[2,2,3,4],[5,6,4],[8,9,10]]
#  # length of LL -> 10. k ->3. len(chunks) = 11/3 = floor(3.666) = 3,  10 % 3 = 2 if remainder, add ele to chunk, and decrement remainder. 

# 2 -> 2 -> 3 -> 4 -> 5 -> 6 -> 4 -> 8 -> 9 -> 10, k = 2 should return [[2,2,3,4,5],[6,4 8,9,10]]
    # length of LL -> 10. k ->2. len(chunks) = 5
    # len(LL) / k = len(chunk)

# empty, k=5
# 5 empty arrays
