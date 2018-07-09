# https://leetcode.com/problems/subarray-product-less-than-k/description/
class Solution:
    def numSubarrayProductLessThanK_DP(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # DP
        # dp[i][j] is the product from i-th to j-th
        # dp[i][j] = dp[i][j-1] * nums[j]
        count = 0
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for i, c in enumerate(nums):
            dp[i][i] = c
            if dp[i][i] < k:
                count += 1

        for length in range(2, len(nums) + 1):
            for i in range(len(nums) - length + 1):
                j = i + length - 1
                if dp[i][j-1] >= k or nums[j] >= k:
                    # Already bigger than or equal to k, just ignore
                    dp[i][j] = k
                else:
                    dp[i][j] = dp[i][j-1] * nums[j]
                    if dp[i][j] < k:
                        count += 1

        return count

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0

        # Greedy Two Pointers
        count, start, prod = 0, 0, 1
        for i, c in enumerate(nums):
            prod *= c
            while prod >= k:
                prod //= nums[start]
                start += 1
            count += i - start + 1

        return count



s = Solution()
nums = [10, 5, 2, 6]
k = 100
print(s.numSubarrayProductLessThanK(nums, k))