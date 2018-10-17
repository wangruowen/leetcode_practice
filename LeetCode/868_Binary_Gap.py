# https://leetcode.com/problems/binary-gap/
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        last_i, cur_i = -1, 0
        max_dist = 0
        while cur_i < 32:
            mask = 1 << cur_i
            if N & mask == mask:
                if last_i >= 0:
                    max_dist = max(max_dist, cur_i - last_i)
                last_i = cur_i
            cur_i += 1
        return max_dist
