# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Same element must gather together as parent or child
        # DFS Preorder Traversal
        node_with_occur_nums = {}
        self.DFS(root, node_with_occur_nums)
        max_modes_values = []
        max_modes_count = float('-inf')
        for each in node_with_occur_nums:
            count = node_with_occur_nums[each]
            if count > max_modes_count:
                max_modes_count = count
                max_modes_values = [each]
            elif count == max_modes_count:
                max_modes_values.append(each)

        return max_modes_values

    def DFS(self, node, occur_dict):
        if node is None:
            return

        if node.val in occur_dict:
            occur_dict[node.val] += 1
        else:
            occur_dict[node.val] = 1

        if node.left:
            self.DFS(node.left, occur_dict)
        if node.right:
            self.DFS(node.right, occur_dict)


