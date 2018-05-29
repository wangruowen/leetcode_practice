# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # DFS In-order traversal
        self._visit_count = k
        return self.helper(root)

    def helper(self, node):
        if not node:
            return None

        left_result = self.helper(node.left)
        if left_result is not None:
            return left_result

        self._visit_count -= 1
        if self._visit_count == 0:
            return node.val

        right_result = self.helper(node.right)
        if right_result is not None:
            return right_result

        return None