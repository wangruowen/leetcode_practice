# https://leetcode.com/problems/distribute-candies/description/
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # If kinds < half of the number of candies,
        # then, sister take each kind, and sum up to half num
        # If kinds >= half, then take half
        kinds = len(set(candies))
        if kinds < len(candies) / 2:
            return kinds
        else:
            return len(candies) / 2
