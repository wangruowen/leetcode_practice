# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # To make it a linked list in-place,
        # We flatten the left child and right child,
        # Then we move left node to be the new right node, and append previous right node
        def helper(node):
            if not node:
                return None

            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

            old_right = node.right
            node.right = node.left
            last, cur = None, node
            while cur:
                last, cur = cur, cur.right
            last.right = old_right
            node.left = None

            return node

        helper(root)

    def __init___v2(self):
        self.prev = None

    def flatten_v2(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
