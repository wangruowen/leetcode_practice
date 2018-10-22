# https://www.programcreek.com/2014/08/leetcode-shortest-word-distance-iii/
class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        m, n = -1, -1
        min_dist = float('inf')
        for i, c in enumerate(words):
            if c == word1:
                m = i
                if n >= 0:
                    min_dist = min(min_dist, m - n)
                if word1 == word2:
                    n = m
            elif c == word2:
                n = i
                if m >= 0:
                    min_dist = min(min_dist, n - m)
        return min_dist




s = Solution()
words = ["practice", "makes", "perfect", "coding", "makes", "makes"]
word1, word2 = "makes", "makes"
print(s.shortestWordDistance(words, word1, word2))
