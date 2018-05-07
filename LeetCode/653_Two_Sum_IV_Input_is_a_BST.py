# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # BFS or DFS with set
        if not root:
            return False
        stack = [root]
        visited = set()
        while len(stack) > 0:
            node = stack.pop()
            if k - node.val in visited:
                return True
            else:
                visited.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False



s = Solution()
