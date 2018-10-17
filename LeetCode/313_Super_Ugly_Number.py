# https://leetcode.com/problems/super-ugly-number/description/
import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        min_heap = []
        heapq.heappush(min_heap, 1)
        for _ in range(n):
            cur_ugly = heapq.heappop(min_heap)
            if cur_ugly == 1:
                for each_prime in primes:
                    heapq.heappush(min_heap, cur_ugly * each_prime)
                continue

            for i, each_prime in enumerate(primes):
                if cur_ugly % each_prime == 0:
                    for j in range(i + 1):
                        heapq.heappush(min_heap, cur_ugly * primes[j])
                    break

        return cur_ugly

s = Solution()
n = 12
primes = [2, 7, 13, 19]
print(s.nthSuperUglyNumber(n, primes))
