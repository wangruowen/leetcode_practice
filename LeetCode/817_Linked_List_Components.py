# https://leetcode.com/problems/linked-list-components/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        cur = head
        G = set(G)
        groups = 0
        prev_group = None
        while cur:
            if cur.val in G:
                if prev_group is None:
                    prev_group = cur.val
                    groups += 1
            else:
                # chain break
                if prev_group is not None:
                    prev_group = None
            cur = cur.next

        return groups

s = Solution()
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
G = [0, 1, 3]
print(s.numComponents(head, G))