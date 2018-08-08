# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        last, cur = dummy, head
        while cur:
            has_dup = False
            while cur and cur.next and cur.val == cur.next.val:
                has_dup = True
                cur = cur.next
            if not has_dup:
                last.next = cur
                last = cur
            if cur:
                cur = cur.next

        # In case all items till the last are dup
        last.next = cur

        return dummy.next

