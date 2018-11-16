# https://leetcode.com/problems/contains-duplicate-iii/
DEBUG = True

class TreeNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.is_left_child = False
        self.left = self.right = None


class BST:
    def __init__(self, t):
        self.root = None
        self.node_map = {}
        self.t = t

    def _insert(self, cur_node, insert_node):
        is_within_t = False
        if abs(cur_node.val - insert_node.val) <= self.t:
            if DEBUG:
                print("within_t: ", cur_node.val, insert_node.val)
            is_within_t = True

        if cur_node.val < insert_node.val:
            if cur_node.right:
                is_within_t |= self._insert(cur_node.right, insert_node)
            else:
                cur_node.right = insert_node
                insert_node.parent = cur_node
                insert_node.is_left_child = False
        else:
            if cur_node.left:
                is_within_t |= self._insert(cur_node.left, insert_node)
            else:
                cur_node.left = insert_node
                insert_node.parent = cur_node
                insert_node.is_left_child = True
        return is_within_t

    def insert(self, i, val):
        """
        Everytime we insert, we should add the logic to check if the newly inserted node has at most t
        difference with its parent and its children.
        :param i:
        :param val:
        :return:
        """
        result = False
        node = TreeNode(val)
        if not self.root:
            self.root = node
        else:
            result = self._insert(self.root, node)

        self.node_map[i] = node
        return result

    def _remove(self, node):
        # https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
        # Since we keep parent and children, we can leverage them
        if node.val == 9:
            print("Now let's remove 9")

        if not node.left and not node.right:
            if self.root == node:
                self.root = None
            else:
                if node.is_left_child:
                    node.parent.left = None
                else:
                    node.parent.right = None
        elif not node.left:
            # Then replace with right child
            new_node = node.right
            if node.parent:
                if node.is_left_child:
                    node.parent.left = new_node
                else:
                    node.parent.right = new_node
            new_node.parent = node.parent
            new_node.is_left_child = node.is_left_child
            if self.root == node:
                self.root = new_node
        elif not node.right:
            new_node = node.left
            if node.parent:
                if node.is_left_child:
                    node.parent.left = new_node
                else:
                    node.parent.right = new_node
            new_node.parent = node.parent
            new_node.is_left_child = node.is_left_child
            if self.root == node:
                self.root = new_node
        else:
            replace_node = node.right
            while replace_node.left:
                replace_node = replace_node.left
            # Now replace_node is the most left node in right subtree
            # move replace_node to node's position
            if replace_node.parent != node:
                replace_node.parent.left = replace_node.right

            replace_node.left = node.left
            if replace_node != node.right:
                replace_node.right = node.right
            replace_node.parent = node.parent
            replace_node.is_left_child = node.is_left_child
            if self.root == node:
                self.root = replace_node
            # self._remove(replace_node)


    def remove(self, i):
        if DEBUG:
            print("remove: ", i, self.node_map[i].val)
        self._remove(self.node_map[i])
        # del self.node_map[i]


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Two Pointers, Sliding Window, Sorting with Binary Search Tree
        if k == 0:
            return False

        window_bst = BST(t)
        start = 0
        for i, c in enumerate(nums):
            if i - start <= k:
                if window_bst.insert(i, c):
                    return True
            else:
                window_bst.remove(start)
                start += 1
                if window_bst.insert(i, c):
                    return True
        return False


s = Solution()
# nums = [1,5,9,1,5,9]
# k = 2
# t = 3
nums = [3,6,0,4]
k = 2
t = 2
print(s.containsNearbyAlmostDuplicate(nums, k, t))
