# https://leetcode.com/problems/split-bst/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        """
        Because the TreeNode doesn't have parent pointer, only Recursion can help keep track of the parent children link
        Iterative ways can easily miss the parent children link
        """
        if not root:
            return [None, None]

        while root:
            if V < root.val:
                # root is bigger than V, basically, we need to split the root.left
                smaller, bigger = self.splitBST(root.left, V)
                root.left = bigger
                return [smaller, root]
            elif V > root.val:
                # root is smaller than V, we need to split the root.right
                smaller, bigger = self.splitBST(root.right, V)
                root.right = smaller
                return [root, bigger]
            else:
                # root.val == V
                bigger = root.right
                root.right = None
                return [root, bigger]

