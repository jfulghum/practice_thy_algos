# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            nextNode = curr.next
            while nextNode and curr.val == nextNode.val:
                nextNode = nextNode.next
            curr.next = nextNode
            curr = curr.next
        return head

#     https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
