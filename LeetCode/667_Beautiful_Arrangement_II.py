# https://leetcode.com/problems/beautiful-arrangement-ii/description/
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        # Observation:
        # Given 1, 2, 3, 4, 5
        # 1 (+4) 5 (-3) 2 (+2) 4 (-1) 3 to be k = 4 distinct integers
        # 1 (+3) 4 (-2) 2 (+1) 3 (rest) 5 to be k = 3 distinct integers
        # 1 (+2) 3 (-1) 2 (rest) 4, 5 to be k = 2 distinct integers
        # 1 (+1) 2 (rest) 3, 4, 5 to be k = 1 distinct integers
        result = [1]
        sign = 1
        for i in range(k, 0, -1):
            result.append(result[-1] + i * sign)
            sign = -sign
        if result[1] < n:
            for i in range(result[1] + 1, n + 1):
                result.append(i)
        return result

s = Solution()
print(s.constructArray(6, 1))
