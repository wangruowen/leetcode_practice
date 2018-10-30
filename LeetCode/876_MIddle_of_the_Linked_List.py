# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Standard Fast Slow Pointers
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow