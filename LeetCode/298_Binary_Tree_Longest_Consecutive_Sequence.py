# https://www.geeksforgeeks.org/longest-consecutive-sequence-binary-tree/
INCREASING, DECREASING = 1, -1

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution(object):

    @staticmethod
    def get_max_path_to_root(node, parent, length, direct):
        ret_length = length
        if not node:
            return ret_length

        if direct == INCREASING and node.val == parent.val + 1:
            ret_length = max(Solution.get_max_path_to_root(node.left, node, length + 1, direct),
                             Solution.get_max_path_to_root(node.right, node, length + 1, direct))
        elif direct == DECREASING and node.val == parent.val - 1:
            ret_length = max(Solution.get_max_path_to_root(node.left, node, length + 1, direct),
                             Solution.get_max_path_to_root(node.right, node, length + 1, direct))
        return ret_length

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Recursive
        # 1. an increasing sequence from root to children
        # 2. an decreasing sequence from root to children
        # 3. a sequence across the root. one side is increasing. the other side is decreasing
        if not root:
            return 0

        max_path = max(self.longestConsecutive(root.left), self.longestConsecutive(root.right))
        print("node.val=", root.val, " max_path from children=", max_path)
        left_direct, right_direct = None, None
        max_left_to_root, max_right_to_root = 0, 0
        if root.left:
            if root.left.val == root.val + 1:
                left_direct = INCREASING
            elif root.left.val == root.val - 1:
                left_direct = DECREASING
            max_left_to_root = Solution.get_max_path_to_root(root.left, root, 1, left_direct)
        if root.right:
            if root.right.val == root.val + 1:
                right_direct = INCREASING
            elif root.right.val == root.val - 1:
                right_direct = DECREASING
            max_right_to_root = Solution.get_max_path_to_root(root.right, root, 1, right_direct)

        # Get max_path first from either left to root path or right to root path
        max_path = max(max_path, max_left_to_root, max_right_to_root)
        if left_direct == INCREASING and right_direct == DECREASING or left_direct == DECREASING and right_direct == INCREASING:
            max_path = max(max_path, max_left_to_root + max_right_to_root - 1)

        return max_path


s = Solution()
root = TreeNode(6)
root.right = TreeNode(9)
root.right.left = TreeNode(8)
root.right.right = TreeNode(10)
root.right.right.right = TreeNode(11)
print(s.longestConsecutive(root))
