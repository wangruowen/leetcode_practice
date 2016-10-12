# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list_dummy_head = ListNode(0)
        cur_ptr = new_list_dummy_head
        l1_ptr, l2_ptr = l1, l2
        carry = 0

        i, j = 0, 0
        while l1_ptr is not None and l2_ptr is not None:
            tmp = l1_ptr.val + l2_ptr.val + carry
            if tmp >= 10:
                carry = 1
                tmp -= 10
            else:
                carry = 0
            cur_ptr.next = ListNode(tmp)
            cur_ptr = cur_ptr.next
            l1_ptr, l2_ptr = l1_ptr.next, l2_ptr.next

        while l1_ptr is not None:
            tmp = l1_ptr.val + carry
            if tmp >= 10:
                carry = 1
                tmp -= 10
            else:
                carry = 0
            cur_ptr.next = ListNode(tmp)
            cur_ptr = cur_ptr.next
            l1_ptr = l1_ptr.next

        while l2_ptr is not None:
            tmp = l2_ptr.val + carry
            if tmp >= 10:
                carry = 1
                tmp -= 10
            else:
                carry = 0
            cur_ptr.next = ListNode(tmp)
            cur_ptr = cur_ptr.next
            l2_ptr = l2_ptr.next

        if carry == 1:
            cur_ptr.next = ListNode(carry)

        return new_list_dummy_head.next

