# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Same as 442
        result = []
        for each in nums:
            each = abs(each)
            if nums[each - 1] > 0:
                nums[each - 1] = -nums[each - 1]
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result