# https://leetcode.com/problems/combination-sum-iv/description/
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # DP
        # dp[i] is the num of combinations that add up to i
        # dp[i] = sum(dp[i - nums[k]]) where 0<= k < len(nums)
        nums = set(nums)
        dp = [0 for _ in range(target + 1)]
        for i in range(1, len(dp)):
            if i in nums:
                dp[i] = 1
            for k in nums:
                if i >= k:
                    dp[i] += dp[i - k]

        # print(dp)
        return dp[target]


    def backtracking_TLE_combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Backtracking
        nums.sort()
        total_combins = set()
        self._helper(nums, target, [], total_combins)
        return len(total_combins)

    def _helper(self, nums, target, combins, total_combins):
        if target == 0:
            total_combins.add(tuple(combins))
            return

        for i in nums:
            if i <= target:
                combins.append(i)
                if tuple(combins) not in total_combins:
                    print("target = %d, combins = %s" % (target - i, combins))
                    self._helper(nums, target - i, combins, total_combins)
                combins.pop()

s = Solution()
nums = [1,2,3]
target = 4
print(s.combinationSum4(nums, target))