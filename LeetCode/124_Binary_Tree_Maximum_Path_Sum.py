# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum_tle(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # three cases:
        # 1. max_path occurs in the left tree
        # 2. max_path occurs in the right tree
        # 3. max_path spans across root
        # Get max_path_to_root from both left and right, then compare them
        if not root:
            return float('-inf')

        def get_max_to_root(root):
            if not root:
                return float('-inf')

            return max(get_max_to_root(root.left), get_max_to_root(root.right), 0) + root.val

        max_cross_root = max(get_max_to_root(root.left), 0) + max(get_max_to_root(root.right), 0) + root.val
        max_left, max_right = self.maxPathSum(root.left), self.maxPathSum(root.right)

        return max(max_left, max_right, max_cross_root)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_max_to_root(node):
            if not node:
                return 0
            left = max(0, get_max_to_root(node.left))  # max_to_root could be negative, in which case, we don't use it
            right = max(0, get_max_to_root(node.right))
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)
        get_max_to_root(root)
        return self.max_sum