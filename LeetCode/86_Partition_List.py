# https://leetcode.com/problems/partition-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head, more_head = ListNode(""), ListNode("")
        less_ptr, more_ptr = less_head, more_head
        cur = head
        while cur:
            if cur.val < x:
                less_ptr.next = cur
                less_ptr = cur
            else:
                more_ptr.next = cur
                more_ptr = cur
            cur = cur.next
        less_ptr.next = more_head.next
        more_ptr.next = None
        return less_head.next

s = Solution()
dummy = ptr = ListNode("")
a = [1,4,3,2,5,2]
for i in a:
    ptr.next = ListNode(i)
    ptr = ptr.next
result = s.partition(dummy.next, 3)
ptr = result
while ptr:
    print(ptr.val)
    ptr = ptr.next