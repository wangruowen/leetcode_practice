# https://leetcode.com/problems/path-sum/description/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.sum = sum
        if root is None:
            return False
        # DFS
        return self.DFS(root)

    def DFS(self, node, cur_sum=0):
        cur_sum += node.val
        if node.left is not None and \
                self.DFS(node.left, cur_sum) is True:
            return True
        elif node.right is not None and \
                self.DFS(node.right, cur_sum) is True:
            return True
        elif node.left is None and node.right is None and cur_sum == self.sum:
            return True
        else:
            return False
