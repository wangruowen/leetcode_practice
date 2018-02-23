# https://leetcode.com/problems/hamming-distance/description/
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_xor_y = x ^ y
        hamming_distance = 0
        while x_xor_y != 0:
            hamming_distance += (x_xor_y & 1)
            x_xor_y = x_xor_y >> 1
        return hamming_distance

x = 1
y = 4
s = Solution()
print(s.hammingDistance(x, y))