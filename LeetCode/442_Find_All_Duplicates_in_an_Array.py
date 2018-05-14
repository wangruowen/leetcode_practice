# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Reuse existing space
        # Mark the number at index i - 1 to be negative when encounter i
        result = []
        for num in nums:
            num = abs(num)  # it may already be negative
            if nums[num - 1] < 0:
                # this num is already visited before
                result.append(abs(num))
            else:
                nums[num - 1] = -nums[num - 1]  # Switch to opposite sign

        return result