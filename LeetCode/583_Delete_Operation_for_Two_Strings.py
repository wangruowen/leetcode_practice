# https://leetcode.com/problems/delete-operation-for-two-strings/description/
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # DP
        # dp[i][j] is the min steps for word1[i:] and word2[j:]
        # to be the same
        # dp[i][j] = if word1[i] == word2[j]: dp[i+1][j+1]
        #            if word1[i] != word2[j]: 1 + min(dp[i+1][j], dp[i][j+1])
        dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        return self.helper(word1, word2, 0, 0, dp)

    def helper(self, word1, word2, i, j, dp):
        if dp[i][j] >= 0:
            return dp[i][j]

        if i == len(word1):
            dp[i][j] = len(word2) - j
            return dp[i][j]
        if j == len(word2):
            dp[i][j] = len(word1) - i
            return dp[i][j]

        if word1[i] == word2[j]:
            dp[i][j] = self.helper(word1, word2, i+1, j+1, dp)
        else:
            dp[i][j] = 1 + min(self.helper(word1, word2, i+1, j, dp), self.helper(word1, word2, i, j+1, dp))
        return dp[i][j]

s = Solution()
word1, word2 = "sea", "eat"
print(s.minDistance(word1, word2))