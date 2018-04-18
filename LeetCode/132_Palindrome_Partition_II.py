# https://leetcode.com/problems/palindrome-partitioning-ii/description/
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: return 0
        if len(s) == 2: return 0 if s[0] == s[1] else 1

        # First we need to have a cache to know whether s[i..j] is palindrome
        p = [[False for _ in s] for _ in s]
        for i in xrange(len(s)):
            p[i][i] = True
            if i < len(s) - 1 and s[i] == s[i + 1]:
                p[i][i + 1] = True

        for k in xrange(2, len(s)):
            for i in xrange(len(s) - k):
                p[i][i + k] = p[i + 1][i + k - 1] and s[i] == s[i + k]

        # import pprint
        # pprint.pprint(p)

        # f[n] is the min cut of s[0..n] including n
        # f[n + 1] = min(f[n] + 1 if no palindrome, f[k] + 1 if p[k + 1][n + 1] is true)
        f = [0 for _ in s]
        for i in xrange(1, len(s)):
            if p[0][i]:
                # If the full string is palindrome, then partition is 0
                f[i] = 0
            else:
                # It starts from adding a new partition from f[i - 1]
                f[i] = f[i - 1] + 1

            for k in xrange(1, i):
                # if p[k][i] is palindrome, f[k-1] is the rest partition, plus s[k..i]
                if p[k][i]:
                    f[i] = min(f[i], f[k - 1] + 1)
            print("f[%d] = %d" % (i, f[i]))

        return f[-1]


s = Solution()
a = "cbbbcc"
print(s.minCut(a))