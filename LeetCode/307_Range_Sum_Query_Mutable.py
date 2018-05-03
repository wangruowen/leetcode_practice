# https://leetcode.com/problems/range-sum-query-mutable/description/
# https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
# https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/
#Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # Construct Segment Tree
        def createSegmentTree(nums, start, end):
            if start > end:
                return None
            if start == end:
                n = Node(start, end)
                n.total = nums[start]
                return n

            mid = (start + end) / 2
            root = Node(start, end)
            root.left = createSegmentTree(nums, start, mid)
            root.right = createSegmentTree(nums, mid + 1, end)
            root.total = root.left.total + root.right.total
            return root

        self.root = createSegmentTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start + root.end) / 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            root.total = root.left.total + root.right.total

            return root.total

        return updateVal(self.root, i, val)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) / 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i > mid:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)