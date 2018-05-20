# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # meeting point problem
        nums.sort()
        count = 0
        i, j = 0, len(nums) - 1
        while i < j:
            count += nums[j] - nums[i]
            i += 1
            j -= 1
        return count

s = Solution()
nums = [1,0,0,8,6]
print(s.minMoves2(nums))
