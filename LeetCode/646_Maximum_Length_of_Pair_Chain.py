# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # Greedy First sort on the pair[1]
        pairs.sort(key=lambda x: x[1])
        cur, num = float('-inf'), 0
        for each_pair in pairs:
            if cur < each_pair[0]:
                cur = each_pair[1]
                num += 1
        return num


