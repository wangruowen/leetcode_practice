# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS
        result = []
        queue = [root] if root else []
        while len(queue) > 0:
            result.append(max(map(lambda x:x.val, queue)))
            new_queue = []
            for each in queue:
                if each.left:
                    new_queue.append(each.left)
                if each.right:
                    new_queue.append(each.right)
            queue = new_queue
        return result

    def largestValues_DFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Force DFS Preorder Traversal, get the depth first, and then keep an array indexed by depth
        def get_depth(node):
            if not node:
                return 0
            return 1 + max(get_depth(node.left), get_depth(node.right))

        depth = get_depth(root)
        if depth == 0:
            return []

        array = [float('-inf') for _ in range(depth)]
        def DFS(node, depth=0):
            if not node:
                return
            array[depth] = max(array[depth], node.val)
            DFS(node.left, depth + 1)
            DFS(node.right, depth + 1)

        DFS(root)
        return array

