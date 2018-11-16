# https://leetcode.com/problems/inorder-successor-in-bst/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cur, stack = root, []
        found_p = False
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not found_p:
                if cur == p:
                    found_p = True
            else:
                return cur
            cur = cur.right
        return None

    def inorderSuccessor_recursive(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor_recursive(root.right, p)
        else:
            left = self.inorderSuccessor_recursive(root.left, p)
            return left if left else root
