# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
class Solution:
    def numSubarrayBoundedMax_DP(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        # DP
        # dp[i][j] is the maximum value of subarray from A[i] to A[j]
        # dp[i][j] = max(dp[i][j-1], A[j])
        result = 0
        dp = [[-1 for _ in range(len(A))] for _ in range(len(A))]
        for i, c in enumerate(A):
            dp[i][i] = c
            if L <= c <= R:
                result += 1

        for offset in range(1, len(A)):
            for i in range(len(A) - offset):
                j = i + offset
                dp[i][j] = max(dp[i][j-1], A[j])
                if L <= dp[i][j] <= R:
                    result += 1
        return result

    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        # Two Pointers
        result = 0
        start, end = 0, 0
        last_max_idx = -1
        while start <= end < len(A):
            if last_max_idx < 0:
                if L <= A[end] <= R:
                    last_max_idx = end
                    end += 1
                    result += last_max_idx - start + 1
                elif A[end] > R:
                    start = end + 1
                    end = start
                else:
                    end += 1
            elif A[end] <= R:
                if A[end] >= L:
                    last_max_idx = end
                end += 1

                result += last_max_idx - start + 1
            elif A[end] > R:
                last_max_idx = -1
                start = end + 1
                end = start

        return result


s = Solution()
A = [73,55,36,5,55,14,9,7,72,52]
L = 32
R = 69
print(s.numSubarrayBoundedMax(A, L, R))
