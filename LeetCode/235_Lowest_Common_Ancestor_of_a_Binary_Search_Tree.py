# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # This is a solution that does not assume BST, but just Binary Tree
        NONE_FOUND = 0
        FOUND_P = 1
        FOUND_Q = 2
        FOUND_BOTH = 3
        LCA_node = None

        def helper(node):
            nonlocal LCA_node
            if LCA_node:
                return FOUND_BOTH

            result = NONE_FOUND
            if not node:
                return result
            if node == p:
                result = FOUND_P
            elif node == q:
                result = FOUND_Q

            for each in [node.left, node.right]:
                if each:
                    result |= helper(each)
                    if result == FOUND_BOTH:
                        if not LCA_node:
                            LCA_node = node
                        break
            return result

        helper(root)
        return LCA_node if LCA_node else root

    def lowestCommonAncestor_v2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Leverage BST's feature, LCA should stay at the middle of p and q
        if p.val > q.val:
            p, q = q, p
        while not p.val <= root.val <= q.val:
            if q.val <= root.val:
                root = root.left
            else:
                root = root.right
        return root