# https://leetcode.com/problems/search-insert-position/
import bisect

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)

    def searchInsert_v2(self, nums, target):
        i, j = 0, len(nums)
        while i < j:
            mid = (i + j) // 2
            if target > nums[mid]:
                i = mid + 1
            elif target < nums[mid]:
                j = mid
            else:
                return mid
        if i == len(nums):
            return i
        elif target > nums[i]:
            return i + 1
        else:
            return i


