import pprint


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def printTree(self, root):
        """
        result = [["" for _ in range(width)] for _ in range(height)]
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if root is None:
            return [""]

        # First, get the height, and width of the tree using BFS
        height = 1
        width = 1
        queue = [root]
        while len(queue) > 0:
            new_queue = []
            for each in queue:
                if each.left is not None:
                    new_queue.append(each.left)
                if each.right is not None:
                    new_queue.append(each.right)
            queue = new_queue
            if len(queue) > 0:
                # Full node number at this layer plus inherited node number from the last layer
                width += 2 ** height
                height += 1

        result = [[None for _ in range(width)] for _ in range(height)]
        is_first_row = True
        for row in range(height):
            if is_first_row:
                result[row][width / 2] = root
                is_first_row = False
            else:
                for i in range(width):
                    each_last_node = result[row - 1][i]
                    if each_last_node is not None:
                        if each_last_node.left is not None:
                            result[row][i - 2 ** (height - row - 1)] = each_last_node.left
                        if each_last_node.right is not None:
                            result[row][i + 2 ** (height - row - 1)] = each_last_node.right

        # Finally, change node to str(val)
        for row in range(height):
            for col in range(width):
                if result[row][col] is None:
                    result[row][col] = ""
                else:
                    result[row][col] = str(result[row][col].val)

        return result


s = Solution()
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(4)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
pprint.pprint(s.printTree(root), indent=1)
