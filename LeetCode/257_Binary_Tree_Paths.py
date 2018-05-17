# https://leetcode.com/problems/binary-tree-paths/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # DFS
        result = []
        self.helper(root, [], result)
        return result

    def helper(self, node, path, result):
        if not node:
            return

        path.append(node.val)
        if not node.left and not node.right:
            result.append("->".join(map(str, path)))
        else:
            if node.left:
                self.helper(node.left, path, result)
            if node.right:
                self.helper(node.right, path, result)
        path.pop()

