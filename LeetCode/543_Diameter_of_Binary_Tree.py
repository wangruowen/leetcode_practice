# https://leetcode.com/problems/diameter-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS Post-order Traversal
        self.helper(root)
        return self.diameter

    def helper(self, node):
        if not node:
            return 0
        if node.left:
            left_val = self.helper(node.left) + 1
        else:
            left_val = 0
        if node.right:
            right_val = self.helper(node.right) + 1
        else:
            right_val = 0
        node.val = max(left_val, right_val)
        self.diameter = max(self.diameter, left_val + right_val)
        return node.val
