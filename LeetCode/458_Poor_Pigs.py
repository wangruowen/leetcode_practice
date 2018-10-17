# https://leetcode.com/problems/poor-pigs/description/
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        import math
        return int(math.ceil(math.log(buckets) / math.log(minutesToTest/minutesToDie + 1)))