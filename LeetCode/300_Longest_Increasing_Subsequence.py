# https://leetcode.com/problems/longest-increasing-subsequence/description/
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Imagine a hash map with different lengths as each keys and
        # queues as values
        # DP
        # dp[len] keeps the minimum value of subsequence with length "len"
        if len(nums) == 0: return 0
        dp = [nums[0]]
        for each in nums[1:]:
            if each > dp[-1]:
                dp.append(each)
            elif each < dp[0]:
                dp[0] = each
            else:
                for i in range(1, len(dp)):
                    if dp[i - 1] < each and each <= dp[i]:
                        dp[i] = each
                        break

        return len(dp)

s = Solution()
a = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(a))


