# https://leetcode.com/problems/remove-linked-list-elements/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        init_node = ListNode(0)
        last_ptr, cur_ptr = init_node, head
        last_ptr.next = head
        while cur_ptr is not None:
            tmp = cur_ptr.next
            if cur_ptr.val == val:
                last_ptr.next = tmp
            else:
                last_ptr = cur_ptr
            cur_ptr = tmp
        return init_node.next

s = Solution()
test_head = ListNode(1)
test_head.next = ListNode(2)
test_head.next.next = ListNode(6)
test_head.next.next.next = ListNode(3)
print(s.removeElements(test_head, 6))