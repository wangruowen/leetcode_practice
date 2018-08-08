# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        new_cur = RandomListNode(-1)
        cur = head
        new_head = new_cur
        cur_dict, new_dict = {}, {}
        while cur:
            new_cur.next = RandomListNode(cur.label)
            new_cur = new_cur.next
            if cur.random:
                if cur.random in cur_dict:
                    new_cur.random = new_dict[cur_dict[cur.random]]
                else:
                    cur_dict[cur.random] = cur
                    new_dict[cur] = RandomListNode(cur.random.label)
                    new_cur.random = new_dict[cur]
            cur = cur.next

        return new_head.next


