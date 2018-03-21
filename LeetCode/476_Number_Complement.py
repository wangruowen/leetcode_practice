# https://leetcode.com/problems/number-complement/description/
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        reverse_mask_len = len(bin(num)) - 2
        reverse_mask = int('0b' + '1' * reverse_mask_len, 2)
        return num ^ reverse_mask

s = Solution()
print(s.findComplement(5))