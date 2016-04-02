__author__ = 'ruowen.wang'
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp
        return last