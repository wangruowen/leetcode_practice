# https://leetcode.com/problems/reverse-bits/
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        new_n = 0
        for i in range(32):
            new_n |= (n >> i) & 1
            if i < 31:
                new_n <<= 1
        return new_n

s = Solution()
a = s.reverseBits(43261596)
print(a)
