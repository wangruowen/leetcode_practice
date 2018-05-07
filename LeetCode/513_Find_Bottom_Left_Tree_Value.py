# https://leetcode.com/problems/find-bottom-left-tree-value/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS
        queue = [root]
        first_left = None
        while len(queue) > 0:
            new_queue = []
            first_left = None
            while len(queue) > 0:
                node = queue.pop(0)
                if not first_left:
                    first_left = node
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue

        return first_left.val