# https://leetcode.com/problems/positions-of-large-groups/description/
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) <= 1:
            return []

        result = []
        start_point = 0
        for i in range(len(S)):
            if i == len(S) - 1 or S[i] != S[i + 1]:
                if i - start_point >= 2:
                    result.append([start_point, i])
                start_point = i + 1
        return result

s = Solution()
S = "abbxxxxzzy"
print(s.largeGroupPositions(S))
