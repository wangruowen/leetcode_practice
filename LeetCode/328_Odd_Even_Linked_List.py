# https://leetcode.com/problems/odd-even-linked-list/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # We can also use two fast pointers
        if not head:
            return head

        odd_head = head
        even_head = head.next
        if not even_head:
            return head

        odd_cur, even_cur = odd_head, even_head
        cur = even_cur
        is_even = True
        while cur:
            tmp = cur.next
            if is_even:
                odd_cur.next = tmp
                if tmp:
                    odd_cur = tmp
                is_even = False
            else:
                even_cur.next = tmp
                if tmp:
                    even_cur = tmp
                is_even = True
            cur = tmp
        odd_cur.next = even_head
        even_cur.next = None

        return odd_head

s = Solution()
node = ListNode(1)
head = node
for i in range(2, 9):
    node.next = ListNode(i)
    node = node.next
node = s.oddEvenList(head)
result = []
# node = head
while node:
    result.append(str(node.val))
    node = node.next
print("->".join(result))
