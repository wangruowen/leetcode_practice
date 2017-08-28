# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.level_result = []
        self._helper([root])
        return self.level_result

    def _helper(self, bfs_queue):
        val_list = []
        new_bfs_queue = []
        for each_node in bfs_queue:
            val_list.append(each_node.val)
            if each_node.left is not None:
                new_bfs_queue.append(each_node.left)
            if each_node.right is not None:
                new_bfs_queue.append(each_node.right)
        self.level_result.append(val_list)
        if len(new_bfs_queue) > 0:
            self._helper(new_bfs_queue)

s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(s.levelOrder(root))