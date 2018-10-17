# https://leetcode.com/problems/find-median-from-data-stream/description/
class TreeNode:
    # Use a Binary Search Tree that keeps parent, left, right
    # with add and next, prev functions
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left, self.right = None, None

    def add(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = TreeNode(value, self)
            else:
                self.right.add(value)
        else:
            if self.left is None:
                self.left = TreeNode(value, self)
            else:
                self.left.add(value)

    def next(self):
        if self.right:
            node = self.right
            while node.left:
                node = node.left
        else:
            node = self  # if self is already root, node will be None
            while node and node.parent and node == node.parent.right:
                node = node.parent
            if node:
                node = node.parent  # should be left out of previous node, get its parent
        return node

    def prev(self):
        if self.left:
            node = self.left
            while node.right:
                node = node.right
        else:
            node = self
            while node and node.parent and node == node.parent.left:
                node = node.parent
            if node:
                node = node.parent
        return node

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = None
        self.cur = None
        self.n = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.root:
            self.root = TreeNode(num)
            self.cur = self.root
            self.n = 1
            return
        self.root.add(num)
        self.n += 1

        # self.cur points to the current median node
        # if odd, then the exact median
        # if even, then the first node of the two median nodes
        if self.n % 2 == 1:
            if self.cur.value <= num:
                self.cur = self.cur.next()
        else:
            if self.cur.value > num:
                self.cur = self.cur.prev()

    def findMedian(self):
        """
        :rtype: float
        """
        if self.n % 2 == 1:
            return self.cur.value
        else:
            return (self.cur.value + self.cur.next().value) / 2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
