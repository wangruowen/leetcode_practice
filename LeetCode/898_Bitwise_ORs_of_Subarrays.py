# https://leetcode.com/problems/bitwise-ors-of-subarrays/
class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # brute force
        result, cur = set(), {0}
        for i in A:
            cur = {i} | {i | j for j in cur}
            result |= cur
        return len(result)


s = Solution()
A = [1,2,4]
print(s.subarrayBitwiseORs(A))