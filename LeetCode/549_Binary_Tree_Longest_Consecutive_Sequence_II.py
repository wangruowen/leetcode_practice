# http://www.cnblogs.com/grandyang/p/6864398.html
INCREASE, DECREASE = 1, -1

class Solution(object):
    def __init__(self):
        self.cache = {}

    def get_max_seq_to_root(self, root, length, direct):
        if not root:
            return length

        result = length
        for each_child in [root.left, root.right]:
            if each_child and each_child.val == root.val + 1 * direct:
                result = max(result, self.get_max_seq_to_root(each_child, length + 1, direct))

        return result

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Same as 298 Binary Tree Longest Consecutive Sequence
        # Three cases:
        # 1. Longest Sequence in left sub tree
        # 2. Longest Sequence in right sub tree
        # 3. Span across left tree and right tree, through root node
        #    one side is increasing order, the other side is decreasing order
        if not root:
            return 0

        if root in self.cache:
            return self.cache[root]

        max_len = max(1, self.longestConsecutive(root.left), self.longestConsecutive(root.right))
        max_children_len, children_directs = [], []
        for each_child in [root.left, root.right]:
            if each_child:
                direct = None
                if each_child.val == root.val + 1:
                    direct = INCREASE
                elif each_child.val == root.val - 1:
                    direct = DECREASE
                if direct:
                    max_children_len.append(self.get_max_seq_to_root(root, 1, direct))
                    children_directs.append(direct)
        if len(max_children_len) > 0:
            max_len = max(max_len, max(max_children_len))
        if len(children_directs) == 2 and children_directs[0] * children_directs[1] == -1:
            # One side is INCREASE, the other side is DECREASE
            max_len = max(max_len, max_children_len[0] + max_children_len[1] - 1)

        self.cache[root] = max_len
        return max_len

    def longestConsecutive2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def helper(node, direct):
            # helper gets the max length to this root, either left or right
            if not node:
                return 0
            max_left = max_right = 0
            if node.left and node.left.val == node.val + direct:
                max_left = helper(node.left, direct) + 1
            if node.right and node.right.val == node.val + direct:
                max_right = helper(node.right, direct) + 1
            return max(max_left, max_right)

        return max(self.longestConsecutive2(root.left), self.longestConsecutive2(root.right), helper(root, 1) + helper(root, -1) + 1)

