#!/usr/bin/env python
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
def print_list(head):
    cur = head
    list_str = ""
    while cur is not None:
        list_str += str(cur.val) + "->"
        cur = cur.next
    print(list_str[:-2])

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        len = 0
        cur = head
        while cur is not None:
            cur = cur.next
            len += 1
        if len < 3: return

        second_half_ptr = head
        tmp_len = 1
        pass_mid_len = len / 2 + 2
        # if len is odd, like 5, last should be len / 2 + 1 = 3, second_half should be len / 2 + 2 = 4
        # if len is even, like 6, last should be len / 2 + 1 = 4, second_half should be len / 2 + 2 = 5
        while tmp_len < pass_mid_len:
            last = second_half_ptr
            second_half_ptr = second_half_ptr.next
            tmp_len += 1
        last.next = None

        # print_list(second_half_ptr)

        # Reverse
        last = None
        while second_half_ptr is not None:
            tmp = second_half_ptr.next
            second_half_ptr.next = last
            last = second_half_ptr
            second_half_ptr = tmp
        second_half_ptr = last

        # print_list(second_half_ptr)

        first_half_ptr = head
        while second_half_ptr is not None:
            first_half_last = first_half_ptr
            first_half_ptr = first_half_last.next
            second_half_last = second_half_ptr
            second_half_ptr = second_half_last.next

            first_half_last.next = second_half_last
            second_half_last.next = first_half_ptr


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    Solution().reorderList(head)

    print_list(head)
