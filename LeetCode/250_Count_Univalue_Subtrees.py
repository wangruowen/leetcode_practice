# https://leetcode.com/problems/count-univalue-subtrees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS PostOrder Traversal Bottom Up
        result = 0
        def helper(node):
            nonlocal result
            if not node:
                return None

            left_val = right_val = node.val
            if node.left:
                left_val = helper(node.left)
            if node.right:
                right_val = helper(node.right)
            if left_val == right_val == node.val:
                result += 1
                return node.val
            else:
                return None
        helper(root)
        return result
