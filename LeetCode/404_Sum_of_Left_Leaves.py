# https://leetcode.com/problems/sum-of-left-leaves/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS
        total = 0
        if not root:
            return total

        if root.left:
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)
        if root.right:
            total += self.sumOfLeftLeaves(root.right)

        return total

    def sumOfLeftLeaves_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if not root:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                if not node.left.left and not node.left.right:
                    result += node.left.val
                else:
                    stack.append(node.left)
        return result
