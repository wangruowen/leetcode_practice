# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS, the goal is to find the first and last non-None nodes
        if not root: return 0
        queue = [root]
        max_width = 1
        while queue:
            new_queue = []
            for node in queue:
                if len(new_queue) == 0:
                    # The new queue is still empty
                    # If cur node has children, we can start recording the first child
                    if node:
                        if node.left:
                            new_queue.append(node.left)
                            # Once the left starts, append right no matter it is None or not
                            new_queue.append(node.right)
                        elif node.right:
                            new_queue.append(node.right)
                else:
                    # The new queue already starts with some children
                    # Append None as placeholder for Null nodes in between
                    if node:
                        new_queue.append(node.left)
                        new_queue.append(node.right)
                    else:
                        new_queue.append(None)
                        new_queue.append(None)
            # Pop out None nodes in the end
            while new_queue and new_queue[-1] is None:
                new_queue.pop()
            max_width = max(max_width, len(new_queue))
            queue = new_queue

        return max_width
