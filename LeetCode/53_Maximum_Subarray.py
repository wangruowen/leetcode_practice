# https://leetcode.com/problems/maximum-subarray/description/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # local_max is a positive number that has been added up so far,
        # it is the yet-to-be the potential max after add with the next big num.
        # global_max refers to the current global_max
        # both local_max and global_max can be negative in a mostly negative array
        # In such case, we need to find the smallest negative num
        local_sum_so_far, global_max = nums[0], nums[0]
        for each in nums[1:]:
            local_sum_so_far = max(each, local_sum_so_far + each)
            global_max = max(local_sum_so_far, global_max)

        return global_max
