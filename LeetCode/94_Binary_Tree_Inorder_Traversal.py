# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        traversal_list = []
        if root.left is not None:
            traversal_list.extend(self.inorderTraversal(root.left))
        traversal_list.append(root.val)
        if root.right is not None:
            traversal_list.extend(self.inorderTraversal(root.right))
        return traversal_list

    def inorderTraversal_v2(self, root):
        stack = []
        traversal_list = []
        cur_node = root
        while cur_node is not None:
            if cur_node.left is not None:
                tmp_node = cur_node
                cur_node = tmp_node.left
                tmp_node.left = None
                stack.append(tmp_node)  # Mark left is visited
            else:
                traversal_list.append(cur_node.val)
                if cur_node.right is not None:
                    cur_node = cur_node.right
                else:
                    if len(stack) > 0:
                        cur_node = stack.pop()
                    else:
                        break
        return traversal_list

    def inorderTraversal_v3(self, root):
        if not root: return []
        stack = []
        cur = root
        result = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        return result

s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.inorderTraversal_v3(root))
