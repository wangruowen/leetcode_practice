# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # Since int32 at most has 32 bits
        prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        total_count = 0
        for each in range(L, R + 1):
            count = 0
            while each > 0:
                if each & 1 == 1:
                    count += 1
                each >>= 1
            if count in prime_nums:
                total_count += 1
        return total_count

        # return sum(map(lambda x: bin(x).count('1') in prime_nums, range(L, R+1)))
s = Solution()
L, R = 10, 15
print(s.countPrimeSetBits(L, R))
