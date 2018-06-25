# https://leetcode.com/problems/longest-harmonious-subsequence/description/
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort + Two Pointers
        nums.sort()
        max_len = 0
        low_start, high_start = 0, 0
        i = 1
        while i < len(nums):
            if nums[low_start] == nums[i]:
                i += 1
            elif nums[low_start] + 1 == nums[i]:
                if high_start == low_start:
                    high_start = i
                i += 1
            else:
                # print(i)
                if high_start != low_start:
                    # high and low diff exactly 1
                    max_len = max(max_len, i - low_start)
                    low_start = high_start
                    # We don't increment i here, because nums[i] needs to be evaluated again
                else:
                    low_start = high_start = i
                    i += 1
                # print("low_start = %d" % low_start)
                # print("high_start = %d" % high_start)

        if i == len(nums) and \
                nums[low_start] + 1 == nums[i - 1] and nums[high_start] == nums[i-1]:
            # print(low_start)
            max_len = max(max_len, i - low_start)
        return max_len

s = Solution()
nums = [3,2,2,3,2,1,3,3,3,-2,0,3,2,1,0,3,1,0,1,3,0,3,3]
nums.sort()
print(nums)
print(s.findLHS(nums))