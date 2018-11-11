# https://leetcode.com/problems/russian-doll-envelopes/
import bisect

class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Sort width increasing and height decreasing and then Longest Increasing Subsequence
        # on the height, because now width is auto increasing
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            index = bisect.bisect(dp, h, 0)
            if len(dp) == 0 or dp[-1] < h:
                dp.append(h)
            elif index < len(dp):
                if index > 0 and dp[index - 1] == h:
                    continue
                dp[index] = h
        # print(dp)
        return len(dp)


s = Solution()
enve = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]
print(s.maxEnvelopes(enve))