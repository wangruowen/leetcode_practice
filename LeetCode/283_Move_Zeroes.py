# https://leetcode.com/problems/move-zeroes/description/
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        # Two pointers
        # i points to cur, j points to next non-zero
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j == len(nums):
                    break
                if nums[i] == 0 and j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1

    def moveZeroes2(self, nums):
        # Instead of find zeros, we directly assign non-zero
        # sequentially
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1




