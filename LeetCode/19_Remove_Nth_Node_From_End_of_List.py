# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # In one pass, Keep the last n - 1 visited node, once reach the end, remove it
        # A variant of Fast-Slow pointers
        new_head = ListNode(None)
        new_head.next = head
        back_n_minus_1_ptr = new_head
        cur = new_head
        count = 0
        while cur:
            if count <= n:
                count += 1
            else:
                back_n_minus_1_ptr = back_n_minus_1_ptr.next
            cur = cur.next
        # Now remove the node
        back_n_minus_1_ptr.next = back_n_minus_1_ptr.next.next
        return new_head.next

