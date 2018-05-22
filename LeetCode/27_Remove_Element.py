# https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Two pointers
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            # Find next non-val item
            while j < len(nums) and nums[j] == val:
                j += 1
            if j == len(nums):
                # Cannot find non-val
                break

            nums[i] = nums[j]
            i += 1
            j += 1
        return i

