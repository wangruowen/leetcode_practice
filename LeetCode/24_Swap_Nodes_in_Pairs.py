# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur:
            p1 = cur.next
            if not p1:
                break
            p2 = p1.next
            if not p2:
                break
            p3 = p2.next
            cur.next = p2
            p2.next = p1
            p1.next = p3
            cur = p1
        return dummy.next



