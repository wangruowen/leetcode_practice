# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self._sec_min = 2 ** 32 - 1

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS find the next value bigger than the root
        self.helper(root)
        if self._sec_min < 2**32 - 1:
            return self._sec_min
        else:
            return -1

    def helper(self, node):
        if not node:
            return

        # each node has exactly two or zero children
        if node.left:
            # First, try the same value child, then the bigger value child
            if node.val == node.left.val:
                first, next = node.left, node.right
            else:
                first, next = node.right, node.left

            if first.val == next.val:
                # If both children are the same, then we have to visit both
                self.helper(first)
                self.helper(next)
            else:
                # first.val < next.val
                # visit first and then compare with next.val
                self.helper(first)
                self._sec_min = min(self._sec_min, next.val)

    def findSecondMinimumValue_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        sec_min = float('inf')
        stack = [root]  # If both children are the same, we have to explore one by one
        while stack:
            cur = stack.pop()
            if cur.left:
                if cur.val == cur.left.val and cur.val < cur.right.val:
                    sec_min = min(sec_min, cur.right.val)
                    stack.append(cur.left)
                elif cur.val == cur.right.val and cur.val < cur.left.val:
                    sec_min = min(sec_min, cur.left.val)
                    stack.append(cur.right)
                elif cur.val == cur.left.val == cur.right.val:
                    stack.append(cur.left)
                    stack.append(cur.right)

        return sec_min if sec_min != float('inf') else -1

    def findSecondMinimumValue_v2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # The root should be the smallest
        # One child should be the same as root,
        # The other child should be bigger than root
        # Then the second min is min(findSecondMin(root.left), root.right)
        if not root or (not root.left and not root.right):
            return -1

        if root.left.val == root.right.val:
            left_second_min = self.findSecondMinimumValue(root.left)
            right_second_min = self.findSecondMinimumValue(root.right)
            if left_second_min < 0 and right_second_min < 0:
                return -1
            elif left_second_min < 0:
                return right_second_min
            elif right_second_min < 0:
                return left_second_min
            else:
                return min(left_second_min, right_second_min)

        elif root.right.val > root.val:
            left_second_min = self.findSecondMinimumValue(root.left)
            if left_second_min < 0:
                return root.right.val
            return min(left_second_min, root.right.val)
        elif root.left.val > root.val:
            right_second_min = self.findSecondMinimumValue(root.right)
            if right_second_min < 0:
                return root.left.val
            return min(right_second_min, root.left.val)



