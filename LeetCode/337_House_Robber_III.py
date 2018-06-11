# https://leetcode.com/problems/house-robber-iii/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # In order not to activate directly-linked nodes,
        # Either choose root with root's grandchild
        # Or choose root.left + root.right
        # DP
        # dp[root] = max(root.val + dp[root.left.left] + dp[root.left.right]
        #                + dp[root.right.left] + dp[root.right.right],
        #                dp[root.right] + dp[root.left])
        dp = {}  # node -> max val if rob the tree with this node as root
        return self._helper(root, dp)

    def _helper(self, node, dp):
        if not node:
            return 0
        if node in dp:
            return dp[node]

        grandchild_max, child_max = node.val, 0
        if node.left:
            child_max += self._helper(node.left, dp)
            if node.left.left:
                grandchild_max += self._helper(node.left.left, dp)
            if node.left.right:
                grandchild_max += self._helper(node.left.right, dp)
        if node.right:
            child_max += self._helper(node.right, dp)
            if node.right.left:
                grandchild_max += self._helper(node.right.left, dp)
            if node.right.right:
                grandchild_max += self._helper(node.right.right, dp)
        dp[node] = max(grandchild_max, child_max)
        return dp[node]










