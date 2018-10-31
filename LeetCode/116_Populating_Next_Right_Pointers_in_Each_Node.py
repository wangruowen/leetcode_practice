# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # BFS
        if not root:
            return
        q = deque([root])
        while q:
            new_q = deque()
            last, node = None, None
            while q:
                last, node = node, q.popleft()
                if last:
                    last.next = node
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return
