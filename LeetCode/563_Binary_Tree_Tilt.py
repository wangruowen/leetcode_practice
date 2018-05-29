# https://leetcode.com/problems/binary-tree-tilt/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.total_tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS Post-order Traversal
        self.DFS(root)
        return self.total_tilt

    def DFS(self, node):
        """
        Return the sum of the node
        :param node:
        :return:
        """
        if not node:
            return 0

        left_sum = self.DFS(node.left)
        right_sum = self.DFS(node.right)
        self.total_tilt += abs(left_sum - right_sum)

        return node.val + left_sum + right_sum

