__author__ = 'Ruowen'
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        last = head
        cur = last.next
        while cur:
            if last.val == cur.val:
                last.next = cur.next
            else:
                last = cur
            cur = cur.next
        return head