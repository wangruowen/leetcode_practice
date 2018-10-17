# https://leetcode.com/problems/split-linked-list-in-parts/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur = root
        length = 0
        while cur:
            length += 1
            cur = cur.next

        result = []
        if length <= k:
            cur = root
            i = 0
            while cur:
                tmp = cur.next
                cur.next = None
                result.append(cur)
                cur = tmp
                i += 1
            while i < k:
                result.append(None)
                i += 1

            return result

        # n % k is from 0 to k - 1
        quotient, remainder = divmod(length, k)
        # Evenly assign one from remainder to each part
        cur = root
        while cur:
            head = cur
            last = None
            for _ in range(quotient):
                last = cur
                cur = cur.next
            if remainder > 0:
                last = cur
                cur = cur.next
                remainder -= 1
            last.next = None
            result.append(head)
        return result

def listprint(node):
    result = ""
    while node:
        result += str(node.val)
        node = node.next
    return result

s = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
print([listprint(x) for x in s.splitListToParts(root, 3)])