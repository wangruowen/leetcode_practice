# https://leetcode.com/problems/path-sum-iii/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Keep all sums of each parent along one path
        # if one sum + current val = target, then count one
        if not root:
            return 0

        self.count = 0
        def DFS(node, sums_of_paths):
            new_sums_of_paths = [node.val]
            if node.val == sum:
                self.count += 1
            for each in sums_of_paths:
                if each + node.val == sum:
                    self.count += 1
                new_sums_of_paths.append(each + node.val)
            if node.left:
                DFS(node.left, new_sums_of_paths)
            if node.right:
                DFS(node.right, new_sums_of_paths)

        DFS(root, [])
        return self.count

    def pathSum_v2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        result = 0

        def DFS(node, path_vals=[]):
            nonlocal result
            if not node:
                return

            new_path_vals = [node.val]
            for i in path_vals:
                new_path_vals.append(i + node.val)
            for each in new_path_vals:
                if each == sum:
                    result += 1
            if node.left:
                DFS(node.left, new_path_vals)
            if node.right:
                DFS(node.right, new_path_vals)

        DFS(root)
        return result