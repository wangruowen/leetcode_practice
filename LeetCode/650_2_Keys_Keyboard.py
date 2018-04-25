# https://leetcode.com/problems/2-keys-keyboard/description/
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return 0
        # Factorize N, the steps is the sum(N factors)
        return sum(self.factorize(n))

    def factorize(self, n):
        i = 2
        factors = []
        sqrt_n = n ** 0.5 if n >= 100 else n
        while i <= sqrt_n:
            if n % i == 0:
                factors.append(i)
                n /= i
            else:
                i += 1
        if n != 1:
            factors.append(n) # the last prime
        print(factors)
        return factors

s = Solution()
n = 111
print(s.minSteps(n))