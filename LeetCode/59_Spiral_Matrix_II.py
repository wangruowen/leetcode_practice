# https://leetcode.com/problems/spiral-matrix-ii/description/
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # i = 0
        # i+1 -> i+n to fill i, i to i, n-i-1,
        # i+n+1 -> i+2n-1 to fill i+1, n-i-1 to n-i-1, n-i-1
        # i+2n -> i+3n-2 to fill n-i-1, n-i-2 to n-i-1,i
        # i+3n-1 -> i+4n-3 to fill n-i-2,i to i+1,i
        cur = 1
        result = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n // 2 + 1):
            for j in range(i, n-i):
                result[i][j] = cur
                cur += 1
            for k in range(i+1, n-i):
                result[k][j] = cur
                cur += 1
            for p in range(n-i-2, i-1, -1):
                result[k][p] = cur
                cur += 1
            for q in range(n-i-2, i, -1):
                result[q][p] = cur
                cur += 1
        return result

s = Solution()
print(s.generateMatrix(7))
