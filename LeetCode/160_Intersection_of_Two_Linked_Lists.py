# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        # Make them the same length, because they eventually will merge as the same length
        lenA, lenB = 0, 0
        curA, curB = headA, headB
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next

        curA, curB = headA, headB
        while lenA > lenB:
            curA = curA.next
            lenA -= 1
        while lenB > lenA:
            curB = curB.next
            lenB -= 1
        while curA != curB:
            curA, curB = curA.next, curB.next

        return curA