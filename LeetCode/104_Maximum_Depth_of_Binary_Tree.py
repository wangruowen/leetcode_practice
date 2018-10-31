# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            new_q = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            queue = new_q
            depth += 1
        return depth
