# https://www.lintcode.com/problem/digit-counts/description
class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        counts = 0
        for i in range(n+1):
            if i == 0 and k == 0:
                counts += 1
            while i > 0:
                if i % 10 == k:
                    counts += 1
                i //= 10
        return counts


