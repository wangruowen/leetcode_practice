# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        if not root: return self.sum
        self.DFS(root)
        return self.sum

    def DFS(self, node, path_sum=0):
        path_sum = path_sum * 10 + node.val
        if not node.left and not node.right:
            self.sum += path_sum
            return

        if node.left:
            self.DFS(node.left, path_sum)
        if node.right:
            self.DFS(node.right, path_sum)

