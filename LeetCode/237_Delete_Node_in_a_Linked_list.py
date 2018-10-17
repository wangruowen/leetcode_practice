# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # move the values of later nodes one step up
        cur = node
        last = None
        while cur and cur.next:
            cur.val = cur.next.val
            last, cur = cur, cur.next
        last.next = None
        del cur

s = Solution()
head = ListNode(4)
head.next = ListNode(5)
target = head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
s.deleteNode(target)
cur = head
while cur:
    print(cur.val)
    cur = cur.next
