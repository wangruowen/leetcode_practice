# https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        if not head.next: return True

        # Fast-slow ptrs
        # If total number is even, fast will point to end None,
        # slow will point the n / 2 index, in other words, the starting point of the right half
        # E.g, 1 -> 2 -> 3 -> 4

        # If total number is odd, fast will point to the last,
        # slow will point the n / 2 index, in other words, the mid point of the list
        # E.g, 1 -> 2 -> 3 -> 4 -> 5
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        is_odd = True if fast else False
        if is_odd:
            slow = slow.next

        # Reverse the right half
        last, cur = None, slow
        while cur:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp

        left_half, right_half = head, last
        match = True
        while right_half:
            if left_half.val != right_half.val:
                match = False
                break
            left_half = left_half.next
            right_half = right_half.next

        return match

s = Solution()
a = [1,2,2,1]
head = ListNode(-1)
cur = head
for each in a:
    head.next = ListNode(each)
    head = head.next

print(s.isPalindrome(cur.next))