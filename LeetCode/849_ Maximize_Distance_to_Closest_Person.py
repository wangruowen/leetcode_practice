# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # Get all indices of 1 and then find nearest for each 0
        one_indices = [i for i, c in enumerate(seats) if c == 1]
        cur_one = 0
        max_len = 0
        for i, c in enumerate(seats):
            if c == 1:
                cur_one += 1
            else:
                if cur_one == 0:
                    dist = abs(i - one_indices[cur_one])
                elif cur_one == len(one_indices):
                    dist = abs(i - one_indices[cur_one - 1])
                else:
                    dist = min(abs(i - one_indices[cur_one - 1]), abs(i - one_indices[cur_one]))
                max_len = max(max_len, dist)
        return max_len

