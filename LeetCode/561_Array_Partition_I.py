# https://leetcode.com/problems/array-partition-i/description/
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort it and pick odd ones
        nums.sort()
        return sum([nums[2 * i] for i in range(len(nums) / 2)])
