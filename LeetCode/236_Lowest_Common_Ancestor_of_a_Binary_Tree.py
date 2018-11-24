# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

FOUND_P = 1
FOUND_Q = 2
FOUND_BOTH = 3

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # For Lowest Common Ancestor, there are three cases
        # 1. root is the LCA, thus one is the left and the other in the right
        # 2. both are in the left tree,
        # 3. both are in the right tree
        def helper(node, p, q):
            result = 0
            if not node:
                return result, None

            if node.val == p.val:
                result = FOUND_P
            elif node.val == q.val:
                result = FOUND_Q

            # If either left or right tree found both, just return
            left_result = right_result = 0
            # left_node = right_node = None
            if node.left:
                left_result, left_node = helper(node.left, p, q)
                if left_result == FOUND_BOTH:
                    return left_result, left_node
            if node.right:
                right_result, right_node = helper(node.right, p, q)
                if right_result == FOUND_BOTH:
                    return right_result, right_node

            # If one found in the left and one found in the right, return this node
            result |= left_result | right_result
            if result == FOUND_BOTH:
                return result, node
            else:
                return result, None
        return helper(root, p, q)[1]
