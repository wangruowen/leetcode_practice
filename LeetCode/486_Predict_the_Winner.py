# https://leetcode.com/problems/predict-the-winner/description/
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Minimax
        mem = [[None for _ in xrange(len(nums))] for _ in xrange(len(nums))]
        return self.helper(nums, 0, len(nums) - 1, mem) >= 0

    def helper(self, nums, start, end, mem):
        if not mem[start][end]:
            if start == end:
                mem[start][end] = nums[start]
            else:
                mem[start][end] = max(nums[start] - self.helper(nums, start + 1, end, mem),
                   nums[end] - self.helper(nums, start, end - 1, mem))

        return mem[start][end]

s = Solution()
a = [1,5,2]
print(s.PredictTheWinner(a))