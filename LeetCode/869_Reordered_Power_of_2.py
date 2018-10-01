# https://leetcode.com/problems/reordered-power-of-2/
from collections import Counter

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        cur_2 = 1
        N_len = len(str(N))
        while len(str(cur_2)) < N_len:
            cur_2 *= 2
        candidates = set()
        while len(str(cur_2)) == N_len:
            candidates.add(cur_2)
            cur_2 *= 2
        for each in candidates:
            if Counter(str(each)) == Counter(str(N)):
                return True
        return False

s = Solution()
print(s.reorderedPowerOf2(46))

