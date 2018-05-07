# https://leetcode.com/problems/construct-string-from-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # DFS Preorder Traversal
        return self.helper(t)

    def helper(self, node):
        if not node:
            return ""

        string = str(node.val)
        if node.left or node.right:
            if node.left:
                string += "(" + self.helper(node.left) + ")"
            else:
                string += "()"
            if node.right:
                string += "(" + self.helper(node.right) + ")"

        return string



