# https://leetcode.com/problems/range-sum-query-immutable/description/
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # DP
        # self.sums[i] is the sum from 0 to i-th item
        self.nums = nums
        self.sums = [0] * len(nums)
        if len(nums) > 0:
            self.sums[0] = nums[0]
            for i in xrange(1, len(nums)):
                self.sums[i] = self.sums[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - self.sums[i] + self.nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
