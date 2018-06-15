# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # DP
        # dp[i][j] is the max length subarray for A[:i] and B[:j]
        # ends_with_max[i][j] indicates whether the max length is end with i and j
        # 1. if A[i-1] == B[j-1] and max_length ends with dp[i-1][j-1]
        #     dp[i][j] = 1 + dp[i-1][j-1]
        #     ends_with_max[i][j] = True
        # 2. if A[i-1] != B[j-1] or A[i-1] == B[j-1] but ends_with_max[i-1][j-1] is False
        #     dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # dp[i][j] = max of the above two
        m, n = len(A), len(B)
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # ends_with_max = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        dp_last_i = [0 for _ in range(n + 1)]
        ends_with_last_i = [0 for _ in range(n + 1)]
        for i in range(1, m + 1):
            dp_i = [0 for _ in range(n + 1)]
            ends_with_i = [0 for _ in range(n + 1)]
            for j in range(1, n + 1):
                dp_i[j] = max(dp_last_i[j], dp_i[j - 1])
                if A[i-1] == B[j-1]:
                    ends_with_i[j] = 1 + ends_with_last_i[j-1]
                    dp_i[j] = max(dp_i[j], ends_with_i[j])
            dp_last_i = dp_i
            ends_with_last_i = ends_with_i

        # print("\n".join(map(str, dp)))
        # print("\n".join(map(str, ends_with_max)))
        return dp_last_i[-1]

s = Solution()
A=[1,0,1,0,0,0,0,0,1,1]
B=[1,1,0,1,1,0,0,0,0,0]
# A = [0, 0, 0]
# B = [0, 0,]
print(s.findLength(A, B))

