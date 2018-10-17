# https://leetcode.com/problems/leaf-similar-trees/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # DFS Preorder Traversal
        leaves = []
        stack = [root1]
        while len(stack) > 0:
            node = stack.pop()
            if not node.right and not node.left:
                leaves.append(node.val)
                continue

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        stack = [root2]
        i = 0
        while len(stack) > 0:
            node = stack.pop()
            if not node.right and not node.left:
                if node.val != leaves[i]:
                    return False
                else:
                    i += 1
                continue

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return True

