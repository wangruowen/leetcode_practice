__author__ = 'ruowen.wang'
# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head: return head

        dummy_head = ListNode("Dummy")
        dummy_head.next = head
        prev_m_ptr = dummy_head
        m_cur = head
        i = 1
        while i < m:
            prev_m_ptr = m_cur
            m_cur = m_cur.next
            i += 1
        n_cur = m_cur
        while i < n:
            n_cur = n_cur.next
            i += 1
        next_n_cur = n_cur.next

        # Now just reverse from m to n
        last = next_n_cur
        cur = m_cur
        while cur != next_n_cur:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp
        # Now last == n_cur
        prev_m_ptr.next = last

        return dummy_head.next




