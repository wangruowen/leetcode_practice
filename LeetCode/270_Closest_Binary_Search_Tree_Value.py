# https://leetcode.com/problems/closest-binary-search-tree-value/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        cur = root
        cands = []
        while cur:
            if target == cur.val:
                return cur.val
            elif target > cur.val:
                if cur.right:
                    if target > cur.right.val:
                        cur = cur.right
                    else:
                        cands.append(cur.val)
                        cands.append(cur.right.val)
                        cur = cur.right.left
                else:
                    cands.append(cur.val)
                    break
            else:
                if cur.left:
                    if target < cur.left.val:
                        cur = cur.left
                    else:
                        cands.append(cur.val)
                        cands.append(cur.left.val)
                        cur = cur.left.right
                else:
                    cands.append(cur.val)
                    break
        min_diff, min_val = float('inf'), None
        for each in cands:
            if min_diff > abs(each - target):
                min_diff = abs(each - target)
                min_val = each
        return min_val

    def closestValue_v2_simple(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min_diff, min_val = float('inf'), None
        while root:
            if target == root.val:
                return root.val
            elif target > root.val:
                if min_diff > abs(target - root.val):
                    min_diff = abs(target - root.val)
                    min_val = root.val
                root = root.right
            else:
                if min_diff > abs(target - root.val):
                    min_diff = abs(target - root.val)
                    min_val = root.val
                root = root.left
        return min_val
