# https://leetcode.com/problems/trim-a-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # DFS Pre-order traversal
        return self.helper(root, L, R)


    def helper(self, node, L, R):
        if node is None: return

        if node.val < L:
            # Only need look at the right subtree
            return self.helper(node.right, L, R)
        elif node.val > R:
            # Only need to look at the left subtree
            return self.helper(node.left, L, R)
        else:
            # within the range
            node.left = self.helper(node.left, L, R)
            node.right = self.helper(node.right, L, R)

        return node

s = Solution()
