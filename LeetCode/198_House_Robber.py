# https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dynamic Programming
        # dp[i] is the max amount to rob till i-th item
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        if len(nums) == 0: return 0

        sum_till = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                sum_till[0] = nums[0]
            elif i == 1:
                sum_till[1] = max(nums[0], nums[1])
            else:
                sum_till[i] = max(sum_till[i - 2] + nums[i], sum_till[i - 1])

        return sum_till[-1]
