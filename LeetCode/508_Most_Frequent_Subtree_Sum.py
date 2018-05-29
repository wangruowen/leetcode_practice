# https://leetcode.com/problems/most-frequent-subtree-sum/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_freq = 0
        self.max_freq_sum = []
        self.sum_freq_map = {}

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # DFS Post-order Traversal
        self.helper(root)
        return self.max_freq_sum

    def helper(self, node):
        if not node:
            return 0

        left_sum = self.helper(node.left)
        right_sum = self.helper(node.right)
        node_sum = left_sum + right_sum + node.val
        self.sum_freq_map[node_sum] = self.sum_freq_map.get(node_sum, 0) + 1
        if self.sum_freq_map[node_sum] > self.max_freq:
            self.max_freq = self.sum_freq_map[node_sum]
            self.max_freq_sum = [node_sum]
        elif self.sum_freq_map[node_sum] == self.max_freq:
            self.max_freq_sum.append(node_sum)

        return node_sum
