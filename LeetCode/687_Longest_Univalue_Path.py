# https://leetcode.com/problems/longest-univalue-path/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_length = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Post-order Traversal
        # Four cases:
        # 1. max length in the left subtree
        # 2. max length in the right subtree
        # 3. If left.val == root.val, try left path of the same val
        # 4. If right.val == root.val, try right path of the same val
        if not root:
            return 0

        def helper(node):
            left_longest_to_root = helper(node.left) if node.left else 0
            right_longest_to_root = helper(node.right) if node.right else 0

            if node.left and node.right and node.left.val == node.val == node.right.val:
                # pass through the root
                self.max_length = max(self.max_length, left_longest_to_root + right_longest_to_root + 2)
                return max(left_longest_to_root, right_longest_to_root) + 1
            elif node.left and node.left.val == node.val:
                self.max_length = max(self.max_length, left_longest_to_root + 1)
                return left_longest_to_root + 1
            elif node.right and node.right.val == node.val:
                self.max_length = max(self.max_length, right_longest_to_root + 1)
                return right_longest_to_root + 1
            else:
                return 0

        self.max_length = max(helper(root), self.max_length)
        return self.max_length
