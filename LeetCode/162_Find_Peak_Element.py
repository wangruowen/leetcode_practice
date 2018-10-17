# https://leetcode.com/problems/find-peak-element/description/
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary Search on two middle values, the criterion is
        # if mid_left > mid_right, then we only need to continue on mid_left
        # if mid_left < mid_right, then we only continue on mid_right
        l, r = 0, len(nums) - 1
        while l < r:
            mid_left = (l + r) // 2
            mid_right = mid_left + 1
            if nums[mid_left] < nums[mid_right]:
                l = mid_right
            else:
                r = mid_left
        return l
