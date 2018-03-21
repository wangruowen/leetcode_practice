# https://leetcode.com/problems/merge-two-binary-trees/description/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        t_m_ptr = None
        if t1 is not None and t2 is not None:
            t_m_ptr = TreeNode(t1.val + t2.val)
            t_m_ptr.left = self.mergeTrees(t1.left, t2.left)
            t_m_ptr.right = self.mergeTrees(t1.right, t2.right)
        elif t1 is not None:
            t_m_ptr = TreeNode(t1.val)
            t_m_ptr.left = self.mergeTrees(t1.left, None)
            t_m_ptr.right = self.mergeTrees(t1.right, None)
        elif t2 is not None:
            t_m_ptr = TreeNode(t2.val)
            t_m_ptr.left = self.mergeTrees(None, t2.left)
            t_m_ptr.right = self.mergeTrees(None, t2.right)

        return t_m_ptr

