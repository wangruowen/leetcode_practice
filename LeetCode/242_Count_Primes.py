# https://leetcode.com/problems/count-primes/description/
import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        prime_test = [True] * n  # Init all num as prime
        prime_test[0] = prime_test[1] = False

        for i in xrange(2, n):
            if prime_test[i]:
                prime_test[2 * i:n:i] = [False] * len(prime_test[2 * i:n:i])

        # for i in range(len(prime_test)):
        #     print("%d: %s" % (i, prime_test[i]))

        return sum(prime_test)

s = Solution()
print(s.countPrimes(1500000))


