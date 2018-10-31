# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None
        

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def helper(start, end):
            """
            generate a tree to hold values from start to end - 1
            :param start:
            :param end:
            :return:
            """
            tree_list = []
            if start == end:
                tree_list.append(None)
                return tree_list

            for i in range(start, end):
                left_children = helper(start, i)
                right_children = helper(i + 1, end)
                for l in left_children:
                    for r in right_children:
                        node = TreeNode(i)
                        node.left, node.right = l, r
                        tree_list.append(node)
            return tree_list

        return helper(1, n+1)

