# https://leetcode.com/problems/card-flipping-game/
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        # If the front and back numbers are the same, that card is useless
        # Then we start from smallest number, flip all cards with this number to
        # back, and pick one as x
        useless_nums = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                useless_nums.add(fronts[i])
        min_num = float('inf')
        for i in range(len(fronts)):
            if fronts[i] not in useless_nums:
                min_num = min(min_num, fronts[i])
            if backs[i] not in useless_nums:
                min_num = min(min_num, backs[i])
        return min_num if min_num < float('inf') else 0


s = Solution()
fronts = [1,2,4,4,7]
backs = [1,3,4,1,3]
print(s.flipgame(fronts, backs))