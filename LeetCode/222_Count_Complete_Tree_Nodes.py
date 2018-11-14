# https://leetcode.com/problems/count-complete-tree-nodes/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_height(root):
            height = 0
            cur = root
            while cur:
                height += 1
                cur = cur.left
            return height

        total_height = get_height(root)
        if total_height == 0:
            return 0

        result = 1  # root node
        left_height = total_height - 1
        right_height = get_height(root.right)

        if right_height == left_height:
            # root.right has the same height as root.left, then root.left is fully complete
            # root.right could be partial complete
            result += 2 ** left_height - 1
            result += self.countNodes(root.right)
        elif right_height > 0:
            # root.right is fully complete, because it is already one level less than root.left
            result += 2 ** right_height - 1
            result += self.countNodes(root.left)
        elif right_height == 0:
            # root has no right and only leaf left
            result += 1
        return result


s = Solution()
root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
print(s.countNodes(root))