# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse_list_till(head, end):
            cur, prev = head, None
            while cur != end:
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            head.next = end
            new_head, new_tail = prev, head
            return new_head, new_tail

        dummy = ListNode(-1)
        dummy.next = head
        cur, prev = head, dummy

        count = 0
        start = prev
        while cur:
            if count < k:
                count += 1
                prev, cur = cur, cur.next
            else:
                start.next, tail = reverse_list_till(start.next, cur)
                start = tail  # the tail becomes new start
                count = 0

        if count == k:
            start.next, _ = reverse_list_till(start.next, cur)

        return dummy.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
cur = s.reverseKGroup(head, 2)
result = []
while cur:
    result.append(str(cur.val))
    cur = cur.next
print("->".join(result))






