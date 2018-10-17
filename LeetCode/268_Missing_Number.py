# https://leetcode.com/problems/missing-number/description/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n + 1) * n / 2 - sum(nums)