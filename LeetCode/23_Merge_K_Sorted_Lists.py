# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Priority Queue Heap Sort
        prio_queue = PriorityQueue()
        result_head = ListNode(-1)
        cur = result_head
        for each_head in lists:
            if each_head:
                prio_queue.put((each_head.val, each_head))
        while prio_queue.qsize() > 0:
            first_node = prio_queue.get()[1]
            cur.next = first_node
            cur = cur.next
            if first_node.next:
                prio_queue.put((first_node.next.val, first_node.next))

        return result_head.next

