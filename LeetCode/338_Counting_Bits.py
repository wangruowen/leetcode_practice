# https://leetcode.com/problems/counting-bits/

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bit_list = []
        for i in range(num+1):
            bits = 0
            while i > 0:
                if i & 0x1 == 1:
                    bits += 1
                i >>= 1
            bit_list.append(bits)
        
        return bit_list

    def countBits_v2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(1, num+1):
            # i >> 1 is already visited,
            result.append((i & 1) + result[i >> 1])
        return result

s = Solution()
print(s.countBits_v2(2))