# https://leetcode.com/problems/rotate-function/description/
class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        sum_A = sum(A)
        max_F = 0
        for i, c in enumerate(A):
            max_F += i * c
        cur_F = max_F
        for k in range(1, n):
            prev_F = cur_F
            cur_F = prev_F - (n-1) * A[-k] + sum_A - A[-k]
            max_F = max(max_F, cur_F)
        return max_F

s = Solution()
A = [4, 3, 2, 6]
print(s.maxRotateFunction(A))