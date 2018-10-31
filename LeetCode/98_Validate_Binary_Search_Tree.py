# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Imagine root.right.left
        # It has a lower bound. all root.right.left node must be bigger than root
        # It also has an upper bound, all root.right.left node must be smaller than root.right
        def helper(node, lower_bound, upper_bound):
            if not node:
                return True
            if node.val <= lower_bound or node.val >= upper_bound:
                return False

            if node.left and not helper(node.left, lower_bound, node.val):
                return False
            if node.right and not helper(node.right, node.val, upper_bound):
                return False

            return True

        return helper(root, float('-inf'), float('inf'))
