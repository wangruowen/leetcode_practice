__author__ = 'ruowen.wang'
# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def compare_height(self, node, level):
        if not node: return level
        left_height = self.compare_height(node.left, level + 1)
        right_height = self.compare_height(node.right, level + 1)

        if not left_height or not right_height:
            return False
        elif abs(left_height - right_height) > 1:
            return False
        else:
            return max(left_height, right_height)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if self.compare_height(root, 1) != False else False
