__author__ = 'Ruowen'
# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        len = 0
        cur = head
        while cur is not None:
            cur = cur.next
            len += 1
        if len == 0:
            return head

        k = k % len
        if k == 0:
            return head

        rotate_ptr = head
        tmp_len = 1
        while tmp_len <= len - k:
            last_ptr = rotate_ptr
            rotate_ptr = rotate_ptr.next
            tmp_len += 1

        last_ptr.next = None

        tmp = rotate_ptr
        while tmp is not None:
            last_ptr = tmp
            tmp = tmp.next
        last_ptr.next = head

        return rotate_ptr

