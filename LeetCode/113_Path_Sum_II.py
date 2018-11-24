# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        def DFS(node, stack=[], pathsum=0):
            nonlocal result
            if not node:
                return

            stack.append(node.val)
            pathsum += node.val
            if not node.left and not node.right and pathsum == sum:
                result.append(list(stack))
            else:
                for each in [node.left, node.right]:
                    if each:
                        DFS(each, stack, pathsum)
            stack.pop()

        DFS(root)
        return result