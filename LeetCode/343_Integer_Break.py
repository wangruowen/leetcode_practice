# https://leetcode.com/problems/integer-break/description/
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2

        # DP
        # max_prod[n] is the max product of n's integer break
        # max_prod[n] = max(i * max_prod[n - i]) when 2 <= i <= n - 2
        # because n needs to be broken into at least two positive integers,
        # i is at least 2
        max_prod = [0] * (n + 1)
        max_prod[2] = 1
        max_prod[3] = 2
        max_prod[4] = 4
        for k in xrange(5, n + 1):
            for i in xrange(2, k - 1):
                if k - i <= 3:
                    # Special case for 2 and 3
                    val = k - i
                else:
                    val = max_prod[k - i]
                max_prod[k] = max(max_prod[k], i * val)

        return max_prod[n]

s = Solution()
print(s.integerBreak(10))

