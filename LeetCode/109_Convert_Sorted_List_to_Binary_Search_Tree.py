# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # Fast-slow ptrs to get mid
        last_slow_ptr = None
        fast_ptr, slow_ptr = head, head
        while fast_ptr:
            fast_ptr = fast_ptr.next
            if fast_ptr:
                fast_ptr = fast_ptr.next
                last_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next

        root = TreeNode(slow_ptr.val)
        last_slow_ptr.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow_ptr.next)

        return root

s = Solution()
l_array = [-10, -3, 0, 5, 9]
l = ListNode(-1)
tmp = l
for each in l_array:
    tmp.next = ListNode(each)
    tmp = tmp.next
t = s.sortedListToBST(l.next)

def print_tree(tree, indent=""):
    print(indent + str(tree.val))
    indent += " " * 2
    if tree.left:
        print_tree(tree.left, indent)
    if tree.right:
        print_tree(tree.right, indent)

print_tree(t)