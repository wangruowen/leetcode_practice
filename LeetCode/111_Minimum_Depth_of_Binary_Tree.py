# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS
        if root is None: return 0
        cur_queue = deque([root])
        next_queue = deque()
        depth = 1

        while True:
            while len(cur_queue) > 0:
                cur_node = cur_queue.popleft()
                if cur_node.left is None and cur_node.right is None:
                    return depth
                if cur_node.left is not None:
                    next_queue.append(cur_node.left)
                if cur_node.right is not None:
                    next_queue.append(cur_node.right)
            cur_queue = next_queue
            next_queue = deque()
            depth += 1

