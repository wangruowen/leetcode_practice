# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        max_i = nums.index(max_num)
        for i in range(len(nums)):
            if i == max_i:
                continue
            if nums[i] * 2 > max_num:
                return -1
        return max_i