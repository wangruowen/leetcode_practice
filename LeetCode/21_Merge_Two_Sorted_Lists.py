# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        cur = head
        ptr1, ptr2 = l1, l2
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                cur.next = ptr1
                ptr1 = ptr1.next
            else:
                cur.next = ptr2
                ptr2 = ptr2.next
            cur = cur.next
        while ptr1:
            cur.next = ptr1
            ptr1 = ptr1.next
            cur = cur.next
        while ptr2:
            cur.next = ptr2
            ptr2 = ptr2.next
            cur = cur.next
        return head.next
