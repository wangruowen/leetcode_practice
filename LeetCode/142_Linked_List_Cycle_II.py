# https://leetcode.com/problems/linked-list-cycle-ii/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Refer to https://blog.csdn.net/willduan1/article/details/50938210
        # Fast-slow ptrs
        fast, slow = head, head
        has_cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break

        if not has_cycle:
            return None

        # Reset slow
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next

        return slow
