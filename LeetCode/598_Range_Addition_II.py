# https://leetcode.com/problems/range-addition-ii/description/
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        M_row = [0] * m
        M_col = [0] * n

        for a, b in ops:
            for i in range(a):
                M_row[i] += 1
            for j in range(b):
                M_col[j] += 1

        max_num = M_row[0]
        i, j = 0, 0
        while i < m:
            if M_row[i] != max_num:
                break
            i += 1
        while j < n:
            if M_col[j] != max_num:
                break
            j += 1
        return i * j

s = Solution()
m, n = 40000, 40000
ops = []
print(s.maxCount(m, n, ops))