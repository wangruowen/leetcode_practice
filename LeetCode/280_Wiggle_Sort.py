# https://leetcode.com/problems/wiggle-sort/
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Two Pointers, just follow the rule and fix one by one
        if len(nums) <= 1:
            return

        p1, p2, is_p1_le_p2 = 0, 1, True
        while p2 < len(nums):
            if is_p1_le_p2:
                # nums[p1] <= nums[p2]
                if nums[p1] > nums[p2]:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
            else:
                # nums[p1] >= nums[p2]
                if nums[p1] < nums[p2]:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1
            is_p1_le_p2 = not is_p1_le_p2

