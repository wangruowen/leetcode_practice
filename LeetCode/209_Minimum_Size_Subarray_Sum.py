# https://leetcode.com/problems/minimum-size-subarray-sum/description/
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Two Pointers
        if sum(nums) < s:
            return 0

        start, end = 0, 0
        min_len = len(nums)
        sum_sofar = nums[end]
        while True:
            if sum_sofar >= s:
                min_len = min(min_len, end - start + 1)
                if min_len == 1:
                    # length 1 is the minimum
                    return min_len
                sum_sofar -= nums[start]
                start += 1
            else:
                end += 1
                if end < len(nums):
                    sum_sofar += nums[end]
                else:
                    break
        return min_len

s = Solution()
nums = [2,3,1,2,4,3]
target = 7
print(s.minSubArrayLen(target, nums))