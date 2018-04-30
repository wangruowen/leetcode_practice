# https://leetcode.com/problems/add-two-numbers-ii/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1, len2 = 0, 0
        ptr1, ptr2 = l1, l2
        while ptr1:
            len1 += 1
            ptr1 = ptr1.next
        while ptr2:
            len2 += 1
            ptr2 = ptr2.next

        if len1 < len2:
            l1, l2 = l2, l1
            len1, len2 = len2, len1

        # Now l1 is longer, start from l1
        ptr1, ptr2 = l1, l2
        for _ in range(len1 - len2):
            ptr1 = ptr1.next

        # Now ptr1, ptr2 should be aligned
        for _ in range(len2):
            ptr1.val += ptr2.val
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Now adjust the carry using stack
        stack = []
        ptr1 = l1
        while ptr1:
            stack.append(ptr1)
            ptr1 = ptr1.next

        carry = 0
        while len(stack) > 0:
            cur_node = stack.pop()
            cur_node.val += carry
            if cur_node.val >= 10:
                cur_node.val -= 10
                carry = 1
            else:
                carry = 0
        if carry == 1:
            tmp = ListNode(1)
            tmp.next = l1
            l1 = tmp

        return l1


s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l2 = ListNode(5)
l2.next = ListNode(6)
result = s.addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next





